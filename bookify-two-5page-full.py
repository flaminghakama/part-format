# bookify-two-5page.py

# bookify-two-5page.py input1.pdf input2.pdf output1.pdf output2.pdf

import sys
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger

inputOneFileName = sys.argv[1] 
inputTwoFileName = sys.argv[2] 
outputOneFileName = sys.argv[3] 
outputTwoFileName = sys.argv[4] 
print "input 1: " + inputOneFileName
print "input 2: " + inputTwoFileName 
print "output 1: " + outputOneFileName 
print "output 2: " + outputTwoFileName 

inputReaderOne = PdfFileReader(open(inputOneFileName, "rb"))
inputReaderTwo = PdfFileReader(open(inputTwoFileName, "rb"))
outputWriterOne = PdfFileWriter()
outputWriterTwo = PdfFileWriter()

outputWriterOne.addPage(inputReaderOne.getPage(0))
outputWriterOne.addPage(inputReaderOne.getPage(1))
outputWriterOne.addPage(inputReaderOne.getPage(4))
outputWriterOne.insertBlankPage()
outputStreamOne = file(outputOneFileName, "wb")
outputWriterOne.write(outputStreamOne)

outputWriterTwo.addPage(inputReaderTwo.getPage(0))
outputWriterTwo.addPage(inputReaderTwo.getPage(1))
outputWriterTwo.addPage(inputReaderTwo.getPage(4))
outputWriterTwo.insertBlankPage()
outputStreamTwo = file(outputTwoFileName, "wb")
outputWriterTwo.write(outputStreamTwo)

