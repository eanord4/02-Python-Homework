# Eric Nordstrom
# November 18, 2019
# Second homework assignment for UT Data Analysis & Visualization boot camp
# Python 3.6.4

# "On The Road" is a novel by Jack Kerouac that was originally typed without paragraphing. Therefore, it can be considered one of the longest paragraphs ever written. The published version, used here, uses paragraphs, so this script will clean it to put it into single-paragraph form. Disclaimer: the final result will not actually match the original, single-paragraph version as edits were made before publishing.
# Source: http://www.pauladaunt.com/books/Kerouac,%20Jack%20-%20On%20The%20Road.txt


import re


"""DATA"""

original_text_path = 'C:/Users/eanor.LORDSTROM/Dropbox/Documents/Education/Data Analysis & Viz Boot Camp/Homework/02-Python/PyParagraph/on_the_road.txt'  # path on my computer; change to yours
new_text_path = 'single_paragraph.txt'  # output file path


"""FUNCTIONS"""

def sentences(text):
    '''setences(text) --> split the text into sentences'''

    return re.split("(?<=[.!?]) +", text)

def clean(in_file_path, out_file_path):
    '''clean(in_file_path, out_file_path) --> create output file as a single paragraph, leaving out title page text. NOTE: deletes preexisting output file if present'''

    include = False

    with open(in_file_path, 'r') as in_file, open(out_file_path, 'w') as out_file:  # writes over existing output file if present

        for para in in_file:

            if para == 'ON THE ROAD\n':  # start of text to be included
                include = True

            if include:
                out_file.write(para[:-1] + ' ')  # replace newline with space

def analyze(paragraph_file_path):
    '''analyze(paragraph_file_path) --> print an analysis of the paragraph'''

    with open(paragraph_file_path, 'r') as para_file:
        sents = [sent.split() for sent in sentences(para_file.read())]

    n_sent = n_word = n_char = 0
    
    for sent in sents:

        for word in sent:
            n_char += len(word)
            n_word += 1
        
        n_sent += 1

    avg_sent_len = n_word / n_sent
    avg_letter_count = n_char / n_word

    print('PARAGRAPH ANALYSIS')
    print('------------------')
    print('Approximate Word Count:', n_word)
    print('Approximate Sentence Count:', n_sent)
    print('Average Letter Count:', avg_letter_count)
    print('Average Sentence Length:', avg_sent_len)


"""RUN"""

if __name__ == '__main__':
    print()
    clean(original_text_path, new_text_path)  # create single paragraph file
    analyze(new_text_path)