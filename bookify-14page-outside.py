
# bookify-10page-outside.py input1.pdf output1.pdf [automatic|manual]

# A 14-page booklet has three full pages (outside, middle, inside) 
# and an inside half page.  This script creates a PDF of the full pages. 

#           \          /
#            \        /
#            2\1   14/13
#              \    /
#               \  /  
#  ____3_________\/______ 12_____  
#       4                11
#               /| \
#              / |  \
#           5 /  |   \ 10
#            /6 7|8  9\
#           /    |     \
#          /     |      \

#  The order of pages is based on the 3rd argument.

#  If the 3rd argument is specified as "manual", 
#  the printing order is for manual double-sided printing, 
#  with both outward sides printed first, then the inward sides"
#    Outward outside
#    Middle outside
#    Outward inside
#    Middle inside
 
#  Otherwise, the printing order is intended for automatic double-sided printing:
#    Outward outside
#    Outward inside
#    Middle outside
#    Middle inside

import sys
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger

inputOneFileName = sys.argv[1] 
outputOneFileName = sys.argv[2] 
print "input 1: " + inputOneFileName
print "output 1: " + outputOneFileName 

inputReaderOne = PdfFileReader(open(inputOneFileName, "rb"))
outputWriterOne = PdfFileWriter()

pageIndex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

pageIndex[0] = 13
pageIndex[1] = 0

if sys.argv[3] == "manual":
	pageIndex[2] = 11
	pageIndex[3] = 2
	pageIndex[4] = 9
	pageIndex[5] = 4
	pageIndex[6] = 1
	pageIndex[7] = 12
	pageIndex[8] = 3
	pageIndex[9] = 10

else:
	pageIndex[2] = 1
	pageIndex[3] = 12
	pageIndex[4] = 11
	pageIndex[5] = 2
	pageIndex[6] = 3
	pageIndex[7] = 10
	pageIndex[8] = 9
	pageIndex[9] = 4

pageIndex[10] = 5
pageIndex[11] = 8

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
