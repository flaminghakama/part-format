
# bookify-10page-outside.py input1.pdf output1.pdf [automatic|manual]

# A 10-page booklet has two full pages (outside and middle) 
# and an inside half page.  This script creates a PDF of the full pages. 

#  ____1_________________ 10_____  
#       2                9
#               /| \
#              / |  \
#           3 /  |   \ 8
#            /  5|6   \
#           /    |     \
#          /  4  |    7 \
#

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

pageIndex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

pageIndex[0] = 9
pageIndex[1] = 0

if sys.argv[3] == "manual":
	pageIndex[2] = 7
	pageIndex[3] = 2

	pageIndex[4] = 1
	pageIndex[5] = 8
	pageIndex[6] = 3
	pageIndex[7] = 6

else:
	pageIndex[2] = 1
	pageIndex[3] = 8

	pageIndex[4] = 7
	pageIndex[5] = 2
	pageIndex[6] = 3
	pageIndex[7] = 6

outputWriterOne.addPage(inputReaderOne.getPage(pageIndex[0]))
outputWriterOne.addPage(inputReaderOne.getPage(pageIndex[1]))
outputWriterOne.addPage(inputReaderOne.getPage(pageIndex[2]))
outputWriterOne.addPage(inputReaderOne.getPage(pageIndex[3]))
outputWriterOne.addPage(inputReaderOne.getPage(pageIndex[4]))
outputWriterOne.addPage(inputReaderOne.getPage(pageIndex[5]))
outputWriterOne.addPage(inputReaderOne.getPage(pageIndex[6]))
outputWriterOne.addPage(inputReaderOne.getPage(pageIndex[7]))
outputStreamOne = file(outputOneFileName, "wb")
outputWriterOne.write(outputStreamOne)
