# bookify-8page.py

# bookify-8page.py input1.pdf output1.pdf

#
#  _____1___________________8____
#        2       /\       7
#               /  \
#            3 /    \ 6
#             / 4  5 \
#            /        \
#           /          \
#

#  Printed in the order:  
#    Outward outside
#    Outward inside
#    Inward outside
#    Inward inside

import sys
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger

inputOneFileName = sys.argv[1] 
outputOneFileName = sys.argv[2] 
print "input 1: " + inputOneFileName
print "output 1: " + outputOneFileName 

inputReaderOne = PdfFileReader(open(inputOneFileName, "rb"))
outputWriterOne = PdfFileWriter()

outputWriterOne.addPage(inputReaderOne.getPage(7))
outputWriterOne.addPage(inputReaderOne.getPage(0))
outputWriterOne.addPage(inputReaderOne.getPage(5))
outputWriterOne.addPage(inputReaderOne.getPage(2))
outputWriterOne.addPage(inputReaderOne.getPage(1))
outputWriterOne.addPage(inputReaderOne.getPage(6))
outputWriterOne.addPage(inputReaderOne.getPage(3))
outputWriterOne.addPage(inputReaderOne.getPage(4))
outputStreamOne = file(outputOneFileName, "wb")
outputWriterOne.write(outputStreamOne)
