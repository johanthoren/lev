#!/usr/bin/env python3
import re
import sys
import logging

logging.basicConfig(
    level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

VERSE_RE = re.compile(r'\b([1-9]|[1-9][0-9]|[1-9][0-9][0-9])\b(.+?[^0-9]*)')

V2_RE = re.compile(r'(\\v\s?[2])(\s+.+)')

P = r'\p'


def main():
    i = 1
    for item in sys.argv[1:]:
        text_file = open(sys.argv[i], 'r')
        text_file_name = sys.argv[i]

        print('Working on {}'.format(text_file_name))

        sorted_content = split_text(text_file)
        first_and_second = find_1(sorted_content)

        numbered_content = first_and_second[0]
        chapter_1_known = first_and_second[1]
        false_chapter_2 = first_and_second[2]

        if chapter_1_known is True:
            unclean_content = find_the_rest(numbered_content, false_chapter_2)
        else:
            raise Exception('Unable to find chapters 1 and 2')

        clean_content = clean_up(unclean_content)
        final_content = clean_up(clean_content)

        with open('{}_output.usfm'.format(text_file_name),
                  'w') as text_out_file:
            for x in final_content:
                text_out_file.write('{}\n'.format(x))
        text_out_file.close()
        text_file.close()
        i += 1


def split_text(text_file):
    sorted_content = []
    for line in text_file.readlines():
        verse = VERSE_RE.findall(line)
        if verse:
            for i in verse:
                sorted_content.append(r'\v {} {}'.format(
                    i[0].strip(), i[1].strip()))
            sorted_content.append(r'\p')
        elif line.startswith('Selah'):
            if sorted_content[-1].startswith(r'\p'):
                sorted_content.pop(-1)
            sorted_content.append(r'\qs {}\qs*'.format(line.strip()))
        else:
            sorted_content.append(line.strip())
    return sorted_content


def find_1(sorted_content):
    j = 0
    chapter_1_known = False
    for item in sorted_content:
        v2 = V2_RE.findall(item)
        if v2:
            if chapter_1_known is False:
                logging.debug('Now trying to find chapter 1.')
                for k in range(1, 6):
                    logging.debug('j is %s and k is %s', j, k)
                    potential_chapter_1 = sorted_content[j - k]
                    logging.debug('Potential_chapter_1 is: %s',
                                  potential_chapter_1)
                    if potential_chapter_1.startswith(r'\v 1 '):
                        logging.debug(
                            'found potential_chapter_1: %s',
                            potential_chapter_1,
                        )
                        logging.debug('j is %s and k is %s', j, k)
                        chapter_1_known = True

                        for v in range(1, 4):
                            if sorted_content[(j - k)
                                              + v].startswith('\\v 2 '):
                                false_chapter_2 = sorted_content[(j - k) + v]
                                logging.debug('false_chapter_2 found: %s',
                                              false_chapter_2)
                                break

                        c1 = r'\c 1'

                        if not sorted_content[(j - k) - 1].startswith('\\'):
                            old_string = sorted_content[(j - k) - 1]
                            new_string = '\\s1 ' + old_string
                            sorted_content.pop((j - k) - 1)
                            sorted_content.insert((j - k) - 1, new_string)

                            sorted_content.insert(j - k, P)
                            sorted_content.insert((j - k) - 1, c1)
                        else:
                            sorted_content.insert(j - k, P)
                            sorted_content.insert(j - k, c1)
                        break
            j += 1

    numbered_content = sorted_content
    return (numbered_content, chapter_1_known, false_chapter_2, j)


def find_the_rest(numbered_content, false_chapter_2):
    j = 0
    chapter = 2
    logging.debug('Length of numbered_content is: %s', len(numbered_content))
    while 2 <= len(numbered_content) - j:
        logging.debug('Now trying to find chapter %s.', chapter)
        logging.debug('j is %s', j)
        logging.debug('Remaining entries in numbered_content are: %s',
                      len(numbered_content) - j)

        for item in numbered_content:
            v2 = V2_RE.findall(item)
            if v2:
                try:
                    for k in range(1, 4):
                        potential_chapter = numbered_content[j - k]
                        if potential_chapter == false_chapter_2:
                            logging.debug('Found false positive chapter 2,'
                                          'moving on. Item was: %s',
                                          potential_chapter)
                            break
                        if potential_chapter.startswith(
                                r'\v {} '.format(chapter)):

                            logging.debug(
                                'Testing if the verse is actually the first'
                                'in the chapter: %s', potential_chapter)
                            first = False
                            for l in range(1, 4):
                                n_verse = numbered_content[(j - k) + l]
                                logging.debug('...Testing: %s', n_verse)
                                if n_verse.startswith(r'\v 2 '):
                                    logging.debug('---Success! First verse in'
                                                  'chapter %s found!', chapter)
                                    first = True
                                    break

                            if first is True:
                                logging.debug(
                                    'found potential_chapter: %s',
                                    potential_chapter,
                                )
                                logging.debug('j is %s and k is %s', j, k)

                                c = r'\c {}'.format(chapter)

                                numbered_content = make_verse_one(
                                    numbered_content, j, k, chapter)

                                if not numbered_content[(j - k)
                                                        - 1].startswith('\\'):
                                    numbered_content.insert(j - k, P)
                                    numbered_content.insert((j - k) - 1, c)
                                else:
                                    numbered_content.insert(j - k, P)
                                    numbered_content.insert(j - k, c)

                                chapter += 1
                                break
                            continue
                except IndexError:
                    break
                j += 1
    unclean_content = numbered_content
    return unclean_content


def clean_up(unclean_content):
    i = 0
    for item in unclean_content:
        if item == '':
            unclean_content.pop(i)
        elif not item.startswith('\\'):
            old_string = item
            new_string = '\\s1 ' + old_string
            unclean_content.pop(i)
            unclean_content.insert(i, new_string)
            if unclean_content[i - 1].startswith('\p'):
                unclean_content.pop(i - 1)
                unclean_content.insert(i, r'\p')
        elif item.startswith('\c'):
            if unclean_content[i - 1].startswith('\p'):
                unclean_content.pop(i - 1)
        i += 1

    while unclean_content[-1].startswith(r'\p'):
        unclean_content.pop(-1)

    final_content = unclean_content
    return final_content


def make_verse_one(content, j, k, c):
    old_string = content[j - k]
    new_string = old_string.replace(r'\v {} '.format(c), r'\v 1 ')
    content.pop(j - k)
    content.insert(j - k, new_string)
    return content


main()
