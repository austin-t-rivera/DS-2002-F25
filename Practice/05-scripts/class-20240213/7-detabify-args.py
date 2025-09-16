#!/usr/bin/env python3

import io
import re
import sys

def convert(file_name):

    try:
        # Open new csv file
        csv = io.open(file_name + ".csv", mode="w", encoding="utf-8")
        # Open the tsv file
        with io.open(file_name, mode="r", encoding="utf-8") as tsv:
            for line in tsv:
                csv.write(re.sub('\t',',',re.sub('(^|[\t])([^\t]*\,[^\t\n]*)', r'\1"\2"', line)))
                          
    except FileNotFoundError:
        print('File not found')
        sys.exit(1)

    except Exception as e:
        print('Error:', e)
        sys.exit(1)

    finally:
        csv.close()

if __name__ == '__main__':
    print('Start converting ...')
    if len(sys.argv) < 2:
        print('Usage: python3 detabify-args.py <input file_name>')
        sys.exit(1)
    else:
        file_name = sys.argv[1]
        convert(file_name)
        print('Converted!')
        sys.exit(0)
