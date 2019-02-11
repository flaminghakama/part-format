# bookify-12page.py input1.pdf output1.pdf [automatic|manual]

# A 12-page booklet has three full pages (outside, middle, inside) 

#           \          /
#            \        /
#            2\1   12/11
#              \    /
#               \  /  
#  ____3_________\/______ 10_____  
#       4                 9
#               /  \
#              /    \
#           5 /      \ 8
#            /6      7\
#           /          \
#          /            \

#  The order of pages is based on the 3rd argument.

#  If the 3rd argument is specified as "manual", 
#  the printing order is for manual double-sided printing, 
#  with both outward sides printed first, then the inward sides"
#    Outward outside
#    Middle outside
#    Inner outside
#    Outward inside
#    Middle inside
#    Inner inside 
 
#  Otherwise, the printing order is intended for automatic double-sided printing:
#    Outward outside
#    Outward inside
#    Middle outside
#    Middle inside
#    Inner outside
#    Inner inside 

import sys
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger

inputOneFileName = sys.argv[1] 
outputOneFileName = sys.argv[2] 
print "input 1: " + inputOneFileName
print "output 1: " + outputOneFileName 

inputReaderOne = PdfFileReader(open(inputOneFileName, "rb"))
outputWriterOne = PdfFileWriter()

pageIndex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

pageIndex[0] = 11
pageIndex[1] = 0

if sys.argv[3] == "manual":
    pageIndex[2] = 9
    pageIndex[3] = 2
    pageIndex[4] = 7
    pageIndex[5] = 4
    pageIndex[6] = 1
    pageIndex[7] = 10
    pageIndex[8] = 3
    pageIndex[9] = 8
    pageIndex[10] = 5
    pageIndex[11] = 6

else:
    pageIndex[2] = 9
    pageIndex[3] = 2
    pageIndex[4] = 7
    pageIndex[5] = 4
    pageIndex[6] = 5
    pageIndex[7] = 6
    pageIndex[8] = 3
    pageIndex[9] = 8
    pageIndex[10] = 1
    pageIndex[11] = 10

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
outputStreamOne = file(outputOneFileName, "wb")
outputWriterOne.write(outputStreamOne)
