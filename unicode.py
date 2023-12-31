#!/usr/bin/env python3

# Unicode information


from sys import argv, exit

import unicodedata



# common output

def unicode_info(number, hexnum, char):

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



    try: ucname = unicodedata.name(char)
    except Exception: ucname = 'unknown'

    try: category = categories[unicodedata.category(char)]
    except Exception: category = 'unknown'

    print('Unicode', number, '[hex:', hexnum, ']', 'is:', char,
        '(' + category, '›', ucname + ')')



# cli arg

myname = argv.pop(0).split('/')[-1]

syntax = f'syntax: {myname} <type> <input>\n'
syntax += 'types: s (string), d (decimal), h (hex) or r (range)'

if len(argv) < 2: exit(syntax)

typ, inp = argv[0].lower(), argv[1]

if not typ in 'sdhr': exit(syntax)



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



    # range

    case 'r':
 
        smin, _, smax = inp.partition('-')

        try: imin, imax = int(smin,16), int(smax,16)
        except Exception: exit('syntax: unicode r <hexmin>-<hexmax>')

        for nm in range(imin, imax+1):

            ch = chr(nm)
 
            if ch: print(ch, end=' ')

        print()

