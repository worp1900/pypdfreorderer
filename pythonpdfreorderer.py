#!/usr/bin/python

import sys

from pypdf import PdfWriter, PdfReader

# read input pdf and instantiate output pdf
writer = PdfWriter()
readerFront = PdfReader(sys.argv[1])
readerBack = PdfReader(sys.argv[2])

# page = reader.pages[0]
# print(page.extract_text())

# # construct and shuffle page number list
pagesFront = list(range(readerFront.get_num_pages()))
pagesBack = list(range(readerBack.get_num_pages()))

print('Number of front pages')
print(len(pagesFront))
print('Number of back pages')
print(len(pagesBack))

quit()

# # add the new sequence of pages to output pdf
for page in pages:
    writer.add_page(reader.get_page(page))

# # write the output pdf to file
# outputStream = file(sys.argv[1]+'-mixed.pdf','wb')
writer.write(sys.argv[1]+'-mixed.pdf')
writer.close()
