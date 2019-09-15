# -*- coding: utf-8 -*-

import PyPDF2
import sys

WORD_TO_SEARCH = sys.argv[1].lower()
SOURCE_FILE = sys.argv[2]

file = open(SOURCE_FILE,'rb')
fileReader = PyPDF2.PdfFileReader(file)

for page in range(fileReader.numPages):
    text = fileReader.getPage(page).extractText()
    if WORD_TO_SEARCH in text.lower().replace('\n',''):
        print(page + 1)

file.close()
