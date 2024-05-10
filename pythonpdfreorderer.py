#!/usr/bin/python

import sys

from pypdf import PdfWriter, PdfReader

# read input pdf and instantiate output pdf
writer = PdfWriter()
readerFront = PdfReader(sys.argv[1])
readerBack = PdfReader(sys.argv[2])

counter = 0

# add the new sequence of pages to output pdf
for frontPageNumber in range(len(readerFront.pages)):
    
    backPageNumber = len(readerFront.pages)-1-frontPageNumber

    # Add the front page from the front reader
    writer.append(fileobj=readerFront, pages=(frontPageNumber,frontPageNumber+1))
    # Add the back page from the back reader in inverse order
    writer.append(fileobj=readerBack, pages=(backPageNumber,backPageNumber+1))
    # writer.append(readerBack, readerBack.pages[backPageNumber])

    # Write to an output PDF document
    output = open(sys.argv[1]+'-mixed.pdf', "wb")
    writer.write(output)

# Close file descriptors
writer.close()
output.close()
