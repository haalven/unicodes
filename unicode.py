#! /usr/bin/env python3

# Unicode / utf-8 investigation


from sys import argv, exit
import unicodedata
import copy
import csv
import os


categories = {
    'Lu': 'Uppercase Letter',
    'Ll': 'Lowercase Letter',
    'Lt': 'Titlecase Letter',
    'LC': 'Cased Letter',
    'Lm': 'Modifier Letter',
    'Lo': 'Other Letter',
    'L' : 'Letter',
    'Mn': 'Nonspacing Combining Mark',
    'Mc': 'Spacing Combining Mark',
    'Me': 'Enclosing Combining Mark',
    'M' : 'Mark',
    'Nd': 'Decimal Digit',
    'Nl': 'Letterlike Numeric Character',
    'No': 'Other Numeric Character',
    'N' : 'Number',
    'Pc': 'Connector Punctuation',
    'Pd': 'Dash or Hyphen Punctuation Mark',
    'Ps': 'Opening Punctuation Mark (Pair)',
    'Pe': 'Closing Punctuation Mark (Pair)',
    'Pi': 'Initial Quotation Mark',
    'Pf': 'Final Quotation Mark',
    'Po': 'Other Punctuation',
    'P' : 'Punctuation',
    'Sm': 'Math Symbol',
    'Sc': 'Currency Symbol',
    'Sk': 'Non-letterlike Modifier Symbol',
    'So': 'Other Symbol',
    'S' : 'Symbol',
    'Zs': 'Space Character',
    'Zl': 'Line Separator',
    'Zp': 'Paragraph Separator',
    'Z' : 'Separator',
    'Cc': 'C0/C1 Control Codes',
    'Cf': 'Format Control Character',
    'Cs': 'Surrogate Code Point',
    'Co': 'Private Use Character',
    'Cn': 'Unassigned',
    'C' : 'Other'
}

# ASCII controls (decimal)
controls = {
    0   : 'NUL - Null',
    1   : 'SOH - Start of Heading',
    2   : 'STX - Start of Text',
    3   : 'ETX - End of Text',
    4   : 'EOT - End of Transmission',
    5   : 'ENQ - Enquiry',
    6   : 'ACK - Acknowledgement',
    7   : 'BEL - Bell',
    8   : 'BS - Backspace',
    9   : 'HT - Horizontal Tab',
    10  : 'LF - Line Feed (New Line)',
    11  : 'VT - Vertical Tab',
    12  : 'FF - Form Feed',
    13  : 'CR - Carriage Return',
    14  : 'SO - Shift Out',
    15  : 'SI - Shift In',
    16  : 'DLE - Data Link Escape',
    17  : 'DC1 - Device Control 1',
    18  : 'DC2 - Device Control 2',
    19  : 'DC3 - Device Control 3',
    20  : 'DC4 - Device Control 4',
    21  : 'NAK - Negative Acknowledgement',
    22  : 'SYN - Synchronous Idle',
    23  : 'ETB - End of Transmission Block',
    24  : 'CAN - Cancel',
    25  : 'EM - End of Medium',
    26  : 'SUB - Substitute',
    27  : 'ESC - Escape',
    28  : 'FS - File Separator',
    29  : 'GS - Group Separator',
    30  : 'RS - Record Separator',
    31  : 'US - Unit Separator',
    127 : 'DEL - Delete',
    128 : '<Padding Character> (PAD)',
    129 : '<High Octet Preset> (HOP)',
    130 : '<Break Permitted Here> (BPH)',
    131 : '<No Break Here> (NBH)',
    132 : '<Index> (IND)',
    133 : '<Next Line> (NEL)',
    134 : '<Start of Selected Area> (SSA)',
    135 : '<End of Selected Area> (ESA)',
    136 : '<Character Tabulation Set> (HTS)',
    137 : '<Character Tabulation with Justification> (HTJ)',
    138 : '<Line Tabulation Set> (VTS)',
    139 : '<Partial Line Down> (PLD)',
    140 : '<Partial Line Backward> (PLU)',
    141 : '<Reverse Index> (RI)',
    142 : '<Single Shift Two> (SS2)',
    143 : '<Single Shift Three> (SS3)',
    144 : '<Device Control String> (DCS)',
    145 : '<Private Use One> (PU1)',
    146 : '<Private Use Two> (PU2)',
    147 : '<Set Transmit State> (STS)',
    148 : '<Cancel Character> (CCH)',
    149 : '<Message Waiting> (MW)',
    150 : '<Start of Guarded Area> (SPA)',
    151 : '<End of Guarded Area> (EPA)',
    152 : '<Start of String> (SOS)',
    153 : '<Single Graphic Character Introducer> (SGC)',
    154 : '<Single Character Introducer> (SCI)',
    155 : '<Control Sequence Introducer> (CSI)',
    156 : '<String Terminator> (ST)',
    157 : '<Operating System Command> (OSC)',
    158 : '<Privacy Message> (PM)',
    159 : '<Application Program Command> (APC)'
}


# xterm formatting
def f(code): return '\x1B[' + str(code) + 'm'
def c(code): return f('38;5;' + str(code))


# load Unicode blocks csv
def load_blocks(my_dir):
    blocks_file = os.path.join(my_dir, 'unicode_blocks.csv')
    blocks = []
    with open(blocks_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) >= 3:
                start = int(row[0], 16)
                end = int(row[1], 16)
                name = row[2]
                blocks.append((start, end, name))
    return blocks

# hex value -> Unicode block name
def block_name(hex_string, blocks):
    try:
        # Convert hex string to integer
        code_point = int(hex_string, 16)
        for start, end, name in blocks:
            if start <= code_point <= end:
                return name
        return 'no matching Unicode block found'
    except ValueError:
        return 'invalid hexadecimal input'


# common output
def unicode_info(number, hexnum, char):

    if number in controls:
        ucname = controls[number]
    else:
        try: ucname = unicodedata.name(char)
        except Exception: ucname = 'unknown'

    try: category = categories[unicodedata.category(char)]
    except Exception: category = 'unknown'

    unicode_hex = hexnum[2:].upper()
    while len(unicode_hex) < 4: unicode_hex = '0' + unicode_hex
    unicode_point = f'U+{unicode_hex}'

    byte_seq = ' '.join(f'{b:02x}' for b in char.encode('utf-8'))

    col = 196 if number >= 128 else 44  # ASCII vs higher

    dchar = copy.copy(char)
    dchar = dchar.replace('\b', c(col) + '\\b' + f(39))
    dchar = dchar.replace('\t', c(col) + '\\t' + f(39))
    dchar = dchar.replace('\n', c(col) + '\\n' + f(39))
    dchar = dchar.replace('\v', c(col) + '\\v' + f(39))
    dchar = dchar.replace('\f', c(col) + '\\f' + f(39))
    dchar = dchar.replace('\r', c(col) + '\\r' + f(39))

    print('Unicode',
          c(col) + unicode_point + f(39),
          '(' + str(number) + ')',
          '[' + f(2) + byte_seq + f(22) + ']',
          'is:',
          dchar,
          '(' + block_name(hexnum, blocks),
          '›',
          category,
          '›',
          ucname + ')')


# path
my_path = os.path.abspath(__file__)
my_dir  = os.path.dirname(my_path)

# load blocks
blocks = load_blocks(my_dir)

# cli arg
myname = argv.pop(0).split('/')[-1]

syntax = f'syntax: {myname} <type> <input>\n'
syntax += 'types: s (string), d (decimal), h (hex), b (utf8 byte seq) or r (range)'

if len(argv) < 2: exit(syntax)

typ, inp = argv[0].lower(), argv[1]

if not typ in 'sdhbr': exit(syntax)


match typ:

    # string

    case 's':
        for ch in inp:

            nm = ord(ch)

            hx = hex(nm)

            unicode_info(nm, hx, ch)


    # decimal

    case 'd':

        try: nm = int(inp)
        except Exception: exit('not a decimal number')

        hx = hex(nm)

        ch = chr(nm)

        unicode_info(nm, hx, ch)


    # hexadecimal

    case 'h':

        try: nm = int(inp, 16)
        except Exception: exit('not a hex number')

        hx = hex(nm)

        ch = chr(nm)

        unicode_info(nm, hx, ch)


    # utf8 byte sequence

    case 'b':

        seq = str(inp).replace(' ', '').lower()

        try:
            byte_seq = bytes.fromhex(seq)
        except:
            exit(f'"{seq}" is not a valid hex byte sequence')

        try:
            ch = byte_seq.decode('utf-8')
        except:
            exit(f'{byte_seq} is not a valid utf8 byte sequence')

        nm = ord(ch)

        hx = hex(nm)

        unicode_info(nm, hx, ch)


    # range

    case 'r':

        smin, _, smax = inp.partition('-')

        try: imin, imax = int(smin,16), int(smax,16)
        except Exception: exit('syntax: unicode r <hexmin>-<hexmax>')

        for nm in range(imin, imax+1):

            ch = chr(nm)

            if ch: print(ch, end=' ')

        print()
