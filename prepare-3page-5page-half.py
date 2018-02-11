# prepare-3page-5page-half.py

# prepare-3Page-5Page-half.py input1.pdf input2.pdf output.pdf 

import sys
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger

inputOneFileName = sys.argv[1] 
inputTwoFileName = sys.argv[2] 
outputFileName = sys.argv[3] 
print "input 1: " + inputOneFileName
print "input 2: " + inputTwoFileName 
print "output 1: " + outputFileName 

inputReaderOne = PdfFileReader(open(inputOneFileName, "rb"))
inputReaderTwo = PdfFileReader(open(inputTwoFileName, "rb"))
outputWriter = PdfFileWriter()

# The two half-pages
outputWriter.addPage(inputReaderTwo.getPage(2))
outputWriter.addPage(inputReaderTwo.getPage(3))
outputWriter.addPage(inputReaderOne.getPage(2))
outputWriter.insertBlankPage()
outputStream = file(outputFileName, "wb")
outputWriter.write(outputStream)

