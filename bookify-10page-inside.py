
# bookify-10page-inside.py input1.pdf output1.pdf

# A 10-page booklet has two full pages (outside and middle) 
# and an inside half page.  This script creates a PDF of the half page. 

#  ____1_________________ 10_____  
#       2                9
#               /| \
#              / |  \
#           3 /  |   \ 8
#            /  5|6   \
#           /    |     \
#          /  4  |    7 \
#

import sys
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger

inputOneFileName = sys.argv[1] 
outputOneFileName = sys.argv[2] 
print "input 1: " + inputOneFileName
print "output 1: " + outputOneFileName 

inputReaderOne = PdfFileReader(open(inputOneFileName, "rb"))
outputWriterOne = PdfFileWriter()

outputWriterOne.addPage(inputReaderOne.getPage(4))
outputWriterOne.addPage(inputReaderOne.getPage(5))
outputWriterOne.insertBlankPage()
outputStreamOne = file(outputOneFileName, "wb")
outputWriterOne.write(outputStreamOne)
