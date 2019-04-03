# bookify-16page.py input1.pdf output1.pdf [automatic|manual]

# A 14-page booklet has four full pages, which is like 2 8-page booklets 

#  Outside:
#  ____1_________________16____
#       2       /\      15
#              /  \
#           3 /    \ 14
#            / 4 13 \
#           /        \
#          /          \
#
# Inside:
#  ____5_________________12____
#       6       /\      11
#              /  \
#           7 /    \ 10
#            / 8  9 \
#           /        \
#          /          \
#

#  The order of pages is based on the 3rd argument.

#  If the 3rd argument is specified as "manual", 
#  the intention is to load up a stack of 4 pages, 
#  print the outward sides, then reload the stack 
#  (which is now in reverse order) and print then the inward sides
 
#  Otherwise, the printing order is intended for automatic double-sided printing, 
#  With each page's outward side followed by it's inward side

import sys
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger

inputOneFileName = sys.argv[1] 
outputOneFileName = sys.argv[2] 
print "input 1: " + inputOneFileName
print "output 1: " + outputOneFileName 

inputReaderOne = PdfFileReader(open(inputOneFileName, "rb"))
outputWriterOne = PdfFileWriter()

pageIndex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

pageIndex[0] = 15
pageIndex[1] = 0

if sys.argv[3] == "manual":
    pageIndex[2] = 13
    pageIndex[3] = 2
    pageIndex[4] = 11
    pageIndex[5] = 4
    pageIndex[6] = 9
    pageIndex[7] = 6

    pageIndex[8] = 7
    pageIndex[9] = 8
    pageIndex[10] = 5
    pageIndex[11] = 10
    pageIndex[12] = 3
    pageIndex[13] = 12
    pageIndex[14] = 1
    pageIndex[15] = 14

else:
    pageIndex[2] = 1
    pageIndex[3] = 14
    pageIndex[4] = 13
    pageIndex[5] = 2
    pageIndex[6] = 3
    pageIndex[7] = 12
    pageIndex[8] = 11
    pageIndex[9] = 4
    pageIndex[10] = 5
    pageIndex[11] = 10
    pageIndex[12] = 9
    pageIndex[13] = 6
    pageIndex[14] = 7
    pageIndex[15] = 8

outputWriterOne.addPage(inputReaderOne.getPage(pageIndex[0]))
outputWriterOne.addPage(inputReaderOne.getPage(pageIndex[1]))
outputWriterOne.addPage(inputReaderOne.getPage(pageIndex[2]))
outputWriterOne.addPage(inputReaderOne.getPage(pageIndex[3]))
outputWriterOne.addPage(inputReaderOne.getPage(pageIndex[4]))
outputWriterOne.addPage(inputReaderOne.getPage(pageIndex[5]))
outputWriterOne.addPage(inputReaderOne.getPage(pageIndex[6]))
outputWriterOne.addPage(inputReaderOne.getPage(pageIndex[7]))
outputWriterOne.addPage(inputReaderOne.getPage(pageIndex[8]))
outputWriterOne.addPage(inputReaderOne.getPage(pageIndex[9]))
outputWriterOne.addPage(inputReaderOne.getPage(pageIndex[10]))
outputWriterOne.addPage(inputReaderOne.getPage(pageIndex[11]))
outputWriterOne.addPage(inputReaderOne.getPage(pageIndex[12]))
outputWriterOne.addPage(inputReaderOne.getPage(pageIndex[13]))
outputWriterOne.addPage(inputReaderOne.getPage(pageIndex[14]))
outputWriterOne.addPage(inputReaderOne.getPage(pageIndex[15]))
outputStreamOne = file(outputOneFileName, "wb")
outputWriterOne.write(outputStreamOne)
