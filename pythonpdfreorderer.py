#!/usr/bin/python

import sys
import random

from pypdf import PdfWriter, PdfReader

# read input pdf and instantiate output pdf
writer = PdfWriter()
reader = PdfReader(sys.argv[1])

# page = reader.pages[0]
# print(page.extract_text())

# # construct and shuffle page number list
pages = list(range(reader.get_num_pages()))
random.shuffle(pages)

# # display new sequence
print ('Reordering pages according to sequence:')
print (pages)

# # add the new sequence of pages to output pdf
for page in pages:
    writer.add_page(reader.get_page(page))

# # write the output pdf to file
# outputStream = file(sys.argv[1]+'-mixed.pdf','wb')
writer.write(sys.argv[1]+'-mixed.pdf')
writer.close()
