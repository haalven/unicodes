#! /usr/bin/env python3

# Unicode / utf-8 investigation


from sys import argv, exit
import unicodedata


categories = {
    'Lu': 'Uppercase Letter',
    'Ll': 'Lowercase Letter',
    'Lt': 'Titlecase Letter',
    'LC': 'Cased Letter',
    'Lm': 'Modifier Letter',
    'Lo': 'Other Letter',
    'L' : 'Letter',
    'Mn': 'Nonspacing Mark',
    'Mc': 'Spacing Mark',
    'Me': 'Enclosing Mark',
    'M' : 'Mark',
    'Nd': 'Decimal Number',
    'Nl': 'Letter Number',
    'No': 'Other Number',
    'N' : 'Number',
    'Pc': 'Connector Punctuation',
    'Pd': 'Dash Punctuation',
    'Ps': 'Open Punctuation',
    'Pe': 'Close Punctuation',
    'Pi': 'Initial Punctuation',
    'Pf': 'Final Punctuation',
    'Po': 'Other Punctuation',
    'P' : 'Punctuation',
    'Sm': 'Math Symbol',
    'Sc': 'Currency Symbol',
    'Sk': 'Modifier Symbol',
    'So': 'Other Symbol',
    'S' : 'Symbol',
    'Zs': 'Space Separator',
    'Zl': 'Line Separator',
    'Zp': 'Paragraph Separator',
    'Z' : 'Separator',
    'Cc': 'Control',
    'Cf': 'Format',
    'Cs': 'Surrogate',
    'Co': 'Private Use',
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
    31  : 'US - Unit Separator'
}


# xterm formatting
def f(code): return '\x1B[' + str(code) + 'm'
def c(code): return f('38;5;' + str(code))


# common output
def unicode_info(number, hexnum, char):

    if number in controls:
        ucname = controls[number]
    else:
        try: ucname = unicodedata.name(char)
        except Exception: ucname = 'unknown'

    try: category = categories[unicodedata.category(char)]
    except Exception: category = 'unknown'

    unicode_point = f'U+{hexnum[2:]}'

    byte_seq = ' '.join(f'{b:02x}' for b in char.encode('utf-8'))

    col = 196 if number >= 128 else 44  # ASCII vs higher

    print('Unicode',
          c(col) + unicode_point + f(39),
          '(' + str(number) + ')',
          '[' + f(2) + byte_seq + f(22) + ']',
          'is:',
          char,
          '(' + category,
          '›',
          ucname + ')')


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

        byte_seq = bytes.fromhex(seq)

        ch = byte_seq.decode('utf-8')

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
