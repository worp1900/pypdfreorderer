#!/usr/bin/python

import sys

from pypdf import PdfWriter, PdfReader

# read input pdf and instantiate output pdf
writer = PdfWriter()
readerFront = PdfReader(sys.argv[1])
readerBack = PdfReader(sys.argv[2])
# readerFront = open(sys.argv[1], "rb")
# readerBack = open(sys.argv[2], "rb")

# # construct and shuffle page number list
# pagesFrontInCorrectOrder = list(range(readerFront.get_num_pages()))
# pagesBackInCorrectOrder = list(reversed(list(range(readerBack.get_num_pages()))))

# print('Number of front pages')
# print(len(readerFront.pages))
# print('Number of back pages')
# print(len(readerFront.pages))

# add the new sequence of pages to output pdf
for frontPageNumber in range(len(readerFront.pages)):
    # Add the front page from the front reader
    # writer.append(readerFront, frontPageNumber)
    # Add the back page from the back reader in inverse order
    # writer.append(readerBack, (len(readerFront.pages)-frontPageNumber))
    # print(type(frontPageNumber))

    # print("len(readerFront.pages)")
    # print(len(readerFront.pages))
    # print("range(len(readerFront.pages))")
    # print(range(len(readerFront.pages)))

    # quit()

    backPageNumber = len(readerFront.pages)-1-frontPageNumber

    print("frontPageNumber")
    print(frontPageNumber)
    print("backPageNumber")
    print(backPageNumber)

    # print(readerBack.pages[])

    # backPageNumber = frontPageNumber-1
    # print("backPageNumber")
    # print(backPageNumber)

    # print("readerFront.pages[frontPageNumber]")
    # print(readerFront.pages[frontPageNumber])
    # print("readerBack.pages[backPageNumber]")
    # print(readerBack.pages[backPageNumber])
    # print("readerFront.pages[len(readerFront.pages)-frontPageNumber]")
    # print(readerFront.pages[len(readerFront.pages)-frontPageNumber])
    print("------")

# write the output pdf to file
# outputStream = file(sys.argv[1]+'-mixed.pdf','wb')
# writer.write(sys.argv[1]+'-mixed.pdf')
writer.close()
