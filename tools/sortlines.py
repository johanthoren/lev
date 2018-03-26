#!/usr/bin/env python3
import re
import sys

if len(sys.argv) > 2:
    print('Only able to work on one file.')
    exit(1)

TEXT_FILE = open(sys.argv[1], 'r')
TEXT_FILE_NAME = sys.argv[1]
print('Working on {}'.format(TEXT_FILE_NAME))

verse_re = re.compile(
    r'\b([1-9]|[1-9][0-9]|[1-9][0-9][0-9])\b(.+?[^0-9]*)'
)

def get_text():
    for line in TEXT_FILE.readlines():
        verse = verse_re.findall(line)
        if verse:
            for i in verse:
                print(r'\v {} {}'.format(i[0].strip(), i[1].strip()))
                print(r'\p')
        else:
            print(line.strip())

get_text()
