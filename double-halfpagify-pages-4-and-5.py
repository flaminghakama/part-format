# double-halfpagify-pages-4-and-5.py input1.pdf output1.pdf

import sys
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger

inputOneFileName = sys.argv[1] 
outputOneFileName = sys.argv[2] 
print "input 1: " + inputOneFileName
print "output 1: " + outputOneFileName 

inputReaderOne = PdfFileReader(open(inputOneFileName, "rb"))
outputWriterOne = PdfFileWriter()

outputWriterOne.addPage(inputReaderOne.getPage(4))
outputWriterOne.addPage(inputReaderOne.getPage(3))
outputWriterOne.addPage(inputReaderOne.getPage(4))
outputWriterOne.addPage(inputReaderOne.getPage(3))
outputStreamOne = file(outputOneFileName, "wb")
outputWriterOne.write(outputStreamOne)
