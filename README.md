# PythonPdfReorderer

Python PDF reorderer is a solution for my scanning problems while doing taxes. My printer does not have the option to scan both the front- and backside of a page while running a stack of paper through the document feeder to scan it to my harddrive. It can scan all frontsides of the papers, then turn the stack around and scan all backsides. I end up with two PDFs (front and back), which I resorted to manually merging last year.

Since this is too cumbersome, I wanted to merge them programmatically. While frontsides are fairly straight forward, the backsides are, because the stack of paper is simply turned around and fed through the scanner again, in reverse order:

Consider the following ordering table of pages for a stack of 4 papers:

| frontside  | backside |
| ---------- | -------- |
| 0  | 3  |
| 1  | 2  |
| 2  | 1  |
| 3  | 0  |

Python PDF reorder solves that problem simply by taking the first page of frontpages, then the last page of backpages, then the second of frontpages and the second to last of backpages (and so on) and created a new PDF called "merged.pdf" in the "files" folder. No more need for manual PDF merging.

## Install
Clone the repo, build the image running

    $ docker build docker -t pythonpdfreorderer

You will need two PDF files in the "files" folder: front.pdf and back.pdf.

Run it with

    $ docker run -it --rm --name pypdfreorderer -v "$PWD":/usr/src/myapp -w /usr/src/myapp pythonpdfreorderer:latest python pythonpdfreorderer.py front.pdf back.pdf

## Further references
These are simply for my own reference in the future:
https://hub.docker.com/_/python
https://www.freecodecamp.org/news/python-requirementstxt-explained/
https://pypdf.readthedocs.io/en/stable/user/installation.html
https://superuser.com/questions/655718/randomly-reorder-pages-in-pdf-document
