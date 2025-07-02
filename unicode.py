#! /usr/bin/env python3

# Unicode investigation, version 2
# syntax: unicode2 -TYPE DATA

import sys, os.path, tomllib, argparse, copy, unicodedata, json

DEBUG_LEVEL = 1

# my path
my_path = os.path.abspath(__file__)
my_dir  = os.path.dirname(my_path)
my_name = os.path.basename(my_path)

# load Unicode data
def json_load(filepath):
    with open(filepath, encoding='utf-8') as f:
        return json.load(f)
unicode_blocks = json_load(os.path.join(my_dir, 'unicode_blocks.json'))
codepoint_categories = json_load(os.path.join(my_dir, 'codepoint_categories.json'))
control_codes = json_load(os.path.join(my_dir, 'control_codes.json'))

# xterm formatting
def f(code):
    return '\x1B[' + str(code) + 'm'
def c(code):
    return f('38;5;' + str(code))

# warnings
def warn(msg):
    global DEBUG_LEVEL
    if DEBUG_LEVEL: print(c(196) + str(msg) +f(0),
                          file=sys.stderr)

# read TOML file
def read_configuration(my_dir, my_name):
    c_file = os.path.splitext(my_name)[0] +'.toml'
    c_path = os.path.join(my_dir, c_file)
    if not os.path.exists(c_path):
        warn('config not found at: ' + c_path)
        return None
    try:
        with open(c_path, 'rb') as f:
            return tomllib.load(f)
    except:
        warn('error reading toml: ' + c_path)
        return None

# parse arguments
def get_arguments(my_name):
    parser = argparse.ArgumentParser(prog=my_name)
    # the DATA parameter
    parser.add_argument('DATA',
                        type=str,
                        help='the data to investigate')
    # group contains all possible TYPEs
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-u',
                        action='store_true',
                        help='Unicode point hexadecimal key')
    group.add_argument('-d',
                        action='store_true',
                        help='Unicode point decimal key')
    group.add_argument('-b',
                        action='store_true',
                        help='utf8 byte sequence (hexadecimal)')
    group.add_argument('-s',
                        action='store_true',
                        help='sequence of characters (string)')
    group.add_argument('-r',
                        action='store_true',
                        help='hexadecimal range')
    return parser.parse_args()

# common codepoint information
def print_codepoint_info(decimal, hexnum, char):
    # U+hex key of the codepoint
    unicode_hex = hexnum[2:].upper()
    while len(unicode_hex) < 4:
        unicode_hex = '0' + unicode_hex
    unicode_point = f'U+{unicode_hex}'
    # red (non-ASCII)
    col = 196 if decimal >= 128 else 44
    # utf8 byte sequence
    byte_seq = ' '.join(f'{b:02x}' for b in char.encode('utf-8'))
    # character to print
    ch = copy.copy(char)
    ch = ch.replace('\b', c(col) + '\\b' + f(39))
    ch = ch.replace('\t', c(col) + '\\t' + f(39))
    ch = ch.replace('\n', c(col) + '\\n' + f(39))
    ch = ch.replace('\v', c(col) + '\\v' + f(39))
    ch = ch.replace('\f', c(col) + '\\f' + f(39))
    ch = ch.replace('\r', c(col) + '\\r' + f(39))
    # Unicode block
    block = 'unknown'
    try:
        for start, end, name in unicode_blocks:
            if start <= decimal <= end:
                block = name
    except:
        pass
    # codepoint category
    category = 'unknown'
    try:
        category = codepoint_categories[unicodedata.category(char)]
    except:
        pass
    # Unicode full name
    ucname = 'unknown'
    if decimal in control_codes:
        ucname = control_codes[decimal]
    else:
        try:
            ucname = unicodedata.name(char)
        except:
            pass 
    # print
    print(c(col) + unicode_point + f(39),
        '(' + str(decimal) + ')',
        '[' + f(2) + byte_seq + f(22) + ']',
        'is:',
        ch,
        '(' + block,
        chr(8250),
        category,
        chr(8250),
        ucname + ')')

def main() -> int:
    # load configuration file
    config = read_configuration(my_dir, my_name)
    # get arguments.parameter and arguments.option
    arguments = get_arguments(my_name)
    # Unicode point key (hexadecimal)
    if arguments.u:
        nm = int()
        try:
            nm = int(arguments.DATA, 16)
        except:
            warn(f'{str(arguments.DATA)} is not a hexadecimal number')
        hx = hex(nm)
        ch = chr(nm)
        print_codepoint_info(nm, hx, ch)
    # Decimal Unicode point key
    elif arguments.d:
        try:
            nm = int(arguments.DATA)
        except:
            warn(f'"{str(arguments.DATA)}" is not a decimal number')
            return 1
        hx = hex(nm)
        ch = chr(nm)
        print_codepoint_info(nm, hx, ch)
    # Byte sequence (utf8 hexadecimal)
    elif arguments.b:
        seq = str(arguments.DATA).replace(' ', '').lower()
        try:
            byte_seq = bytes.fromhex(seq)
        except:
            warn(f'"{seq}" is not a valid hex byte sequence')
            return 1
        try:
            ch = byte_seq.decode('utf-8')
        except:
            warn(f'{byte_seq} is not a valid utf8 byte sequence')
            return 1
        nm = ord(ch)
        hx = hex(nm)
        print_codepoint_info(nm, hx, ch)
    # Series of characters (string)
    elif arguments.s:
        for ch in arguments.DATA:
            nm = ord(ch)
            hx = hex(nm)
            print_codepoint_info(nm, hx, ch)
    # Range of Unicode keys
    elif arguments.r:
        smin, _, smax = arguments.DATA.partition('-')
        try:
            imin, imax = int(smin,16), int(smax,16)
        except:
            warn('syntax: unicode r <hexmin>-<hexmax>')
            return 1
        for nm in range(imin, imax + 1):
            if nm in control_codes:
                continue
            ch = chr(nm)
            if ch:
                try:
                    print(ch, end=' ')
                except:
                    continue
        print()
    # exit
    return 0

if __name__ == '__main__':
    sys.exit(main())
