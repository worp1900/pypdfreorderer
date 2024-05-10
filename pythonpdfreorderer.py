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

counter = 0

# add the new sequence of pages to output pdf
for frontPageNumber in range(len(readerFront.pages)):
    
    backPageNumber = len(readerFront.pages)-1-frontPageNumber

    # print("frontPageNumber")
    # print(frontPageNumber)
    # print("backPageNumber")
    # print(backPageNumber)

    # print("readerFront.pages[frontPageNumber]")
    # print(readerFront.pages[frontPageNumber])
    # print("readerBack.pages[backPageNumber])")
    # print(readerBack.pages[backPageNumber])

    # Add the front page from the front reader
    writer.append(fileobj=readerFront, pages=(frontPageNumber,frontPageNumber+1))
    # Add the back page from the back reader in inverse order
    writer.append(fileobj=readerBack, pages=(backPageNumber,backPageNumber+1))
    # writer.append(readerBack, readerBack.pages[backPageNumber])

    # Write to an output PDF document
    output = open(sys.argv[1]+'-mixed.pdf', "wb")
    writer.write(output)

    # if counter == 5:
    #     break
    # counter += 1

# Close file descriptors
writer.close()
output.close()
quit()

# write the output pdf to file
# outputStream = file(sys.argv[1]+'-mixed.pdf','wb')
# writer.write(sys.argv[1]+'-mixed.pdf')
# writer.close()
