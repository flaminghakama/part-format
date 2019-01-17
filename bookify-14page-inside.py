
# bookify-14page-inside.py input1.pdf output1.pdf

# A 14-page booklet has three full pages (outside, middle, inside) 
# and an inside half page.  This script creates a PDF of the half page. 

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

import sys
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger

inputOneFileName = sys.argv[1] 
outputOneFileName = sys.argv[2] 
print "input 1: " + inputOneFileName
print "output 1: " + outputOneFileName 

inputReaderOne = PdfFileReader(open(inputOneFileName, "rb"))
outputWriterOne = PdfFileWriter()

outputWriterOne.addPage(inputReaderOne.getPage(6))
outputWriterOne.addPage(inputReaderOne.getPage(7))
outputWriterOne.insertBlankPage()
outputStreamOne = file(outputOneFileName, "wb")
outputWriterOne.write(outputStreamOne)
