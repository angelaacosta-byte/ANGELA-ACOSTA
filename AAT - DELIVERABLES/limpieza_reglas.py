"""Rule-based screening: parent rolls (bobinas para conversion) vs. finished / unrelated products.
Each record gets KEEP / REMOVE / REVIEW plus the reason, so every deletion is traceable."""
import re

NUM = r'(\d+(?:[.,]\d+)?)'
UNIT = r'(MM|CMS?|MTS?|M)\b'


def _cm(v, unit=None):
    v = float(v.replace(',', '.'))
    if unit is None:                     # unitless: >=300 is almost always mm (e.g. "DIA 1150")
        return v / 10 if v >= 300 else v
    if unit.startswith('MM'):
        return v / 10
    if unit in ('M', 'MT', 'MTS'):
        return v * 100
    return v


def _valid(cm):
    return 5 <= cm <= 300                # drops garbage such as "120020 MM"


def _skip(t, m):
    return re.search(r'(?:NUCLEO|CORE|BUJE|CANUTO)\W{0,3}$', t[max(0, m.start() - 10):m.start()])


def _prep(t):
    t = re.sub(r'(\d),(\d{3})(?!\d)', r'\1\2', t)
    t = re.sub(r',\s*JUMBO\s*,', ', (MARCA), ', t)                   # "JUMBO" used as a brand name
    t = re.sub(r"\b\d\s*X\s*\d{2}\s*['`]|\b\d{2}\s*X\s*\d{2}\s*['`]|\d{2}\s*(?:FT|PIES)\b", ' ', t)  # 20x40' containers
    return t.replace('DIAMTERO', 'DIAMETRO')


def roll_diameter_cm(t):
    vals = []
    lab = r'(?:\bR/?D|\bOD|\bDIAMETER|\bDIA(?:METRO)?(?:\s+(?:DEL\s+)?ROLLO)?(?:\s+INTERIOR)?(?:\s+DE)?|\bD(?:\s*\(MM\))?)'
    for m in re.finditer(rf'{lab}\s*[:=.]?\s*{NUM}\s*(?:{UNIT})?', t):
        if _skip(t, m):
            continue
        u = m.group(2)
        if u is None and m.group(0).find('(MM)') >= 0:
            u = 'MM'
        cm = _cm(m.group(1), u)
        if _valid(cm):
            vals.append(cm)
    for m in re.finditer(rf'{NUM}\s*(MM|CMS?)\s*\(?\s*(?:DE\s+)?(?:DIA(?:METRO)?|OD)\b', t):
        cm = _cm(m.group(1), m.group(2))
        if _valid(cm):
            vals.append(cm)
    # "340MMX76MMX1150MM" or "330MM*1150MM*1*22G" (width x core x diameter)
    for m in re.finditer(r'(\d{3,4})\s*MM\s*[X*]\s*(\d{2,4})\s*MM(?:\s*[X*]\s*(\d{3,4})\s*MM)?', t):
        big = max(int(g) for g in m.groups() if g)
        if big >= 900:
            vals.append(big / 10)
    for m in re.finditer(r'(\d{2,3})\s*CM\s*X\s*(\d{2,3})\s*CM', t):
        big = max(int(m.group(1)), int(m.group(2)))
        if 90 <= big <= 300 and re.search(r'BOBINA|ROLL|ROLLO', t):
            vals.append(big)
    return max(vals) if vals else None


def roll_width_cm(t):
    vals = []
    lab = r'(?:\bR/?W|\bREEL\s*WIDTH|\bANCHO\s+DEL\s+ROLLO|\bANCHOS|\bWIDTH|\bANCHO|\bFORMATO|\bW(?:\s*\(MM\))?|\bF(?=\s*[:=])|\b1F)'
    for m in re.finditer(rf'{lab}\s*[:=.]?\s*{NUM}\s*(?:{UNIT})?', t):
        u = m.group(2)
        if u in ('M', 'MT', 'MTS') and float(m.group(1).replace(',', '.')) >= 10:
            u = 'CM'                      # "RW275M" is a typo for cm in these records
        cm = _cm(m.group(1), u)
        if _valid(cm):
            vals.append(cm)
    for m in re.finditer(rf'{NUM}\s*(MM|CMS?)\s*\(?\s*(?:DE\s+)?(?:ANCHO|WIDE)\b', t):
        cm = _cm(m.group(1), m.group(2))
        if _valid(cm):
            vals.append(cm)
    return max(vals) if vals else None


def big_plain_size_cm(t):
    """Unlabelled sizes like '275CM' or '2800MM' next to tissue/GSM wording."""
    if not re.search(r'GSM|G/M2|GRS?\b|TISSUE|TISU|TOWEL|TOWER|TOALLA|HIGIENICO|SERVILLETA|NAPKIN', t):
        return None
    vals = [_cm(v, u) for v, u in re.findall(r'(\d{2,4})\s*(MM|CMS?)\b', t)]
    vals = [v for v in vals if 90 <= v <= 300]
    return max(vals) if vals else None


KEEP_KW = re.compile(
    r'JUMBO|PARENT\s*ROLL|MOTHER\s*ROLL|\bREELS?\b|BOBINA|PARA\s+(?:LA\s+)?CONVERSION|CONVERTIR|'
    r'FABRICACION\s+DE|PARA\s+(?:LA\s+)?ELABORACION|MATERIA\s+PRIMA|RAW\s+MATERIAL|USO\s*:?\s*INDUSTRIAL|'
    r'PARA\s+LA\s+INDUSTRIA\b(?!\s+DE\s+LA\s+BISUTERIA)|INDUSTRIA\s+PAPELERA|TONELADAS?\s+METRICA|'
    r'CONVERSION|ROLLO\s+MADRE|\d+\s*TM\b|EN\s+KILOGRAMOS|PAPEL\s+BASE|JOB\s+LOT|FABRICACION|PRODUCCION\s+DE|EN\s+TONELADAS|ANCHOS\s*:|'
    r'EN\s+ROLLOS\b.*\b(?:INDUSTRIAL|GSM)|PAPEL\s+INDUSTRIAL|INDUSTRIA\s+DEL\s+PAPEL')

# keep-signals strong enough to win over packing words (e.g. "104 UNIDADES" of parent rolls)
STRONG_KEEP = re.compile(r'ROLLO\s+MADRE|\d+\s*TM\b|INDUSTRIA\s+(?:DEL\s+)?PAPEL|FABRICAC|JUMBO|PARENT\s*ROLL|MOTHER\s*ROLL|PARA\s+(?:LA\s+)?CONVERSION|FABRICACION|MATERIA\s+PRIMA|RAW\s+MATERIAL')

FINISHED_KW = re.compile(
    r'\b\d{2,}\s*(?:HOJAS|SHEETS|SHT|PZS|PZAS|PCS|PIEZAS|UNIDADES|UND|UN|CU)\b|HOJAS\s*/\s*(?:PAQ|BAG)|'
    r'PAQUETES?\b|\bPAQ\b|\bPQTS?\b|\bPACKS?\b|\bPKGS?\b|\d+\s*BAGS?\b|BAGS?\s*/|\bBOLSA\b|BOLSITAS?|'
    r'CAJA\s*(?:X|CONTIENE|DE|CON)|CAJAS\b|POR\s+CAJA|/\s*CASE|(?:POR|X|PER|/)\s*CARTON|\bCTN/|'
    r'INTERFOLI|N\s*FOLD|Z\s*FOLD|DOBLADAS?|CENTER\s*PULL|SHRINK\s*WRAP|'
    r'\d+\s*X\s*\d{3}\s*M\b|(?<![\d.,])\d{2,3}\s*(?:M|MTR|METROS|METERS)\b(?!\s*D)|/ROLL\b|'
    r'\bSET\b|SETS\b|DISPENSADOR|TOALLITAS|PANUELOS|FACIAL|DESMAQUILL|MAQUILLAJE|COSMETOLOG|BOLSON|'
    r'VENTA\s+AL\s+POR\s+MENOR|\bEAN\b|KIRKLAND|\d+-COUNT|INTERFOLEAD|HUGE\s+ROLLS|KITCHEN\s+ROLL\b|'
    r'\d+\s*ROLLS?\s+CARTON|\d+\s*UDS\b|\b\d{2}(?:[.,]\d+)?\s*(?:CM)?\s*[X*]\s*\d{2}(?:[.,]\d+)?\b(?!\s*MM)|'
    r'GUEST\s*TOWELS|SIN\s+VALOR\s+COMERCIAL|USO\s+PERSONAL|COMPRIMIDA|DE\s+19[.,]5\s*CM|MEDIDAS?\s*:\s*19[.,]5|\b\d{2}\s*X\s*\d+\s*X\s*\d+\s*CM|DE\s+\d{2}\s*MTRS|\bCJ\s*X|\d+\s*PCS/|EMBALAJES|\d{2,3}\s*CMS?\s*X\s*\d{2,3}\s*CMS?|\b\d{2}\s*\*\s*\d{2,3}(?!\d)(?!\s*MM)|PAPEL\s+DE\s+CARA|LIMPIAR\s+EL\s+ROSTRO')

UNRELATED_KW = re.compile(
    r'STICKER|ETIQUETA|ROTULO|ROLLO\s+DE\s+CARTON|CARTON\s+F/REEL|SECAMANOS|TORNA[SZ]OL|BLOTTER|TAPETE|'
    r'SALVAMANTEL|RASPADOR|MATIFICANTE|CREPE\s*PAPER|PAPEL\s+CREPADO\s+\d+\s*GSM|MEDICAL|ADORNO|DECORA|'
    r'REGALO|WRAP\s+PAPER|FIESTA|CUMPLEA|MARVEL|DISNEY|FILTRO|LIMPIEZA\s+DE\s+CILINDROS|CARTA\s+CELULOSICA|'
    r'MANTEL|POSA\s*VASO|VASOS?\b|PLATOS?\b|SORBETE|JUGUETE|MANGUERA|CUADERNO|ORIGAMI|PAPEL\s+SEDA|CONFETI|'
    r'BANDERIN|GUIRNALDA|PULSERA|DEPILADOR|WAX\s+PAPER|TELA\s+(?:SIN|NO)\s+TEJ|NO\s+TEJIDA|BISUTERIA|'
    r'VETERINARIO|LECHONES|MASCOTAS|DENTAL|POSTRE|TOALLAS?\s+HUMEDAS|DESINFECTANTE|PLASTICO\b|'
    r'ESTERILIZACION|TERMOSELLADO|GRADO\s+MEDICO|ENVOLTURA|PANOS?\b|RASCADOR|SOBRE\s+PAPEL|RINONERA|\bTINA\b|'
    r'PROTECTOR\s+DE\s+ASIENTO|SEAT\s+COVER|PICADILLO|PARA\s+DUCHA|SHOWER|PARA\s+MEZCLAR|CLOTH|ALGODON|LAVABLE|'
    r'POLIESTER|POLIPROPILENO|ANTIADHERENT|ACEITE|SALONES\s+DE\s+BELLEZA|CABELLO|\bTAG\b|CON\s+LOGO|LOBOTIPO|'
    r'SERVILLETERA|SOPORTE|HOLDER|PARA\s+PLANCHAR|HUMEANTE|VAROMA|PAPELITOS|ACTIVADOR|PARABRISAS|NONWOVEN|'
    r'COTTON|KIT\s+INDUSTRIAL|\bPUFF\b|PROTECCION\s+PERSONAL|HUMIDIFICAD|ARTICULO\s+DE\s+BANO|MINERO|MAQUINARIA|CALENDARIO|ENVELOP|\bLOGO\b|SANITARY\s+NAPKIN|TOALLAS?\s+HIGIENICAS|PANAL')

CONSUMER_KW = re.compile(
    r'USO\s*:?\s*DOMESTICO|ARTICULOS?\s+(?:DEL|PARA\s+EL|DE)\s+HOGAR|HIGIENE\s+PERSONAL|MUESTRA|DONACION|'
    r'VEA\s+FOTO|ARTICULO\s+COMERCIAL|ACCESORIOS?\s+DE\s+BANO|PRIMERA\s+CALIDAD|HAND\s+ROLL|ROLL\s+TOWEL')

MIN_DIAM = 60    # cm: parent rolls are ~100-130 cm; consumer rolls < 25 cm
MIN_WIDTH = 80   # cm: parent-roll widths are ~100-280 cm; consumer rolls < 30 cm


def classify(t):
    t = _prep(t)
    d, w, big = roll_diameter_cm(t), roll_width_cm(t), big_plain_size_cm(t)
    keep, fin = KEEP_KW.search(t), FINISHED_KW.search(t)
    unr, con = UNRELATED_KW.search(t), CONSUMER_KW.search(t)
    if d is not None and d >= MIN_DIAM:
        return 'KEEP', f'diametro de rollo {d:g} cm', d, w
    if unr and not STRONG_KEEP.search(t):
        return 'REMOVE', f'no es papel para conversion: "{unr.group(0).strip()}"', d, w
    if w is not None and w >= MIN_WIDTH and (keep or not fin):
        return 'KEEP', f'ancho de rollo {w:g} cm', d, w
    if big is not None and (keep or not fin):
        return 'KEEP', f'medida de bobina {big:g} cm', d, w
    if d is not None and d < 40 and not STRONG_KEEP.search(t):
        return 'REMOVE', f'diametro {d:g} cm: rollo de consumo', d, w
    if fin and STRONG_KEEP.search(t):
        return 'KEEP', f'senal fuerte de bobina: "{STRONG_KEEP.search(t).group(0).strip()}"', d, w
    if fin and not keep:
        return 'REMOVE', f'producto terminado/empacado: "{fin.group(0).strip()}"', d, w
    if keep and not fin:
        return 'KEEP', f'senal de bobina: "{keep.group(0).strip()}"', d, w
    if keep and fin:
        return 'REVIEW', f'senales mixtas: "{keep.group(0).strip()}" vs "{fin.group(0).strip()}"', d, w
    if con:
        return 'REMOVE', f'producto de consumo sin medidas de bobina: "{con.group(0).strip()}"', d, w
    return 'REVIEW', 'descripcion sin informacion suficiente', d, w
