
# outsideify-6page-as-8page.py input1.pdf output1.pdf

# Outside pages:
#  ____1_________________ -_____  
#       2                -

# ( Inside pages: )
#               /\
#              /  \
#           3 /    \ 6
#            / 4  5 \
#           /        \
#          /          \
#

import sys
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger

inputOneFileName = sys.argv[1] 
outputOneFileName = sys.argv[2] 
print "input 1: " + inputOneFileName
print "output 1: " + outputOneFileName 

inputReaderOne = PdfFileReader(open(inputOneFileName, "rb"))
outputWriterOne = PdfFileWriter()

outputWriterOne.addPage(inputReaderOne.getPage(0))
outputWriterOne.addPage(inputReaderOne.getPage(1))
outputWriterOne.insertBlankPage()
outputStreamOne = file(outputOneFileName, "wb")
outputWriterOne.write(outputStreamOne)
