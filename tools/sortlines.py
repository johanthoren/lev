#!/usr/bin/env python3
import re
import sys

VERSE_RE = re.compile(
    r'\b([1-9]|[1-9][0-9]|[1-9][0-9][0-9])\b(.+?[^0-9]*)'
)

V2_RE = re.compile(r'(\\v\s?[2])(\s+.+)')

def main():
    i = 1
    for item in sys.argv[1:]:
        text_file = open(sys.argv[i], 'r')
        text_file_name = sys.argv[i]

        print('Working on {}'.format(text_file_name))

        content = split_text(text_file)

        with open('{}_output.usfm'.format(text_file_name), 'w') as text_out_file:
            for x in content:
                text_out_file.write('{}\n'.format(x))
        text_out_file.close()
        text_file.close()
        i += 1

def split_text(text_file):
    content = []
    for line in text_file.readlines():
        verse = VERSE_RE.findall(line)
        if verse:
            for i in verse:
                content.append(r'\v {} {}'.format(i[0].strip(), i[1].strip()))
            content.append(r'\p')
        else:
            content.append(line.strip())

    # j = 0
    # for item in content:
    #     v2 = V2_RE.findall(item)
    #     if v2:
    #         print(content[j - 5])
    #         print(content[j - 4])
    #         print(content[j - 3])
    #         print(content[j - 2])
    #         print(content[j - 1])
    #         print(item)
    #     j += 1

    return content

main()
