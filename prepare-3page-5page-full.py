# prepare-3page-5page-full.py

# prepare-3Page-5Page-full.py input1.pdf input2.pdf output.pdf 

import sys
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger

inputOneFileName = sys.argv[1] 
inputTwoFileName = sys.argv[2] 
outputOneFileName = '01-' + sys.argv[3] 
outputTwoFileName = '02-' + sys.argv[3] 
print "input 1: " + inputOneFileName
print "input 2: " + inputTwoFileName 
print "output 1: " + outputOneFileName 
print "output 2: " + outputTwoFileName 

inputReaderOne = PdfFileReader(open(inputOneFileName, "rb"))
inputReaderTwo = PdfFileReader(open(inputTwoFileName, "rb"))
outputWriterOne = PdfFileWriter()
outputWriterTwo = PdfFileWriter()

# From 3-page part, a file for pages 1-2
outputWriterOne.addPage(inputReaderOne.getPage(0))
outputWriterOne.addPage(inputReaderOne.getPage(1))
outputStreamOne = file(outputOneFileName, "wb")
outputWriterOne.write(outputStreamOne)

# From 5-page part, a file for pages 1,2 & 5
outputWriterTwo.addPage(inputReaderTwo.getPage(0))
outputWriterTwo.addPage(inputReaderTwo.getPage(1))
outputWriterTwo.addPage(inputReaderTwo.getPage(4))
outputWriterTwo.insertBlankPage()
outputStreamTwo = file(outputTwoFileName, "wb")
outputWriterTwo.write(outputStreamTwo)

