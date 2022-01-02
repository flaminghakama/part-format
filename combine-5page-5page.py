# combine-5page-5page.py

# combine-5page-page.py input1.pdf input2.pdf output.pdf
# combine two files, so that their last pages split a tabloid page

import sys
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger

inputOneFileName = sys.argv[1] 
inputTwoFileName = sys.argv[2] 
outputOneFileName = sys.argv[3] 
print "input 1: " + inputOneFileName
print "input 2: " + inputTwoFileName 
print "output 1: " + outputOneFileName 

inputReaderOne = PdfFileReader(open(inputOneFileName, "rb"))
inputReaderTwo = PdfFileReader(open(inputTwoFileName, "rb"))
outputWriterOne = PdfFileWriter()

outputWriterOne.addPage(inputReaderOne.getPage(0))
outputWriterOne.addPage(inputReaderOne.getPage(1))
outputWriterOne.addPage(inputReaderOne.getPage(2))
outputWriterOne.addPage(inputReaderOne.getPage(3))
outputWriterOne.addPage(inputReaderOne.getPage(4))
outputWriterOne.addPage(inputReaderTwo.getPage(2))
outputWriterOne.addPage(inputReaderTwo.getPage(0))
outputWriterOne.addPage(inputReaderTwo.getPage(1))
outputStreamOne = file(outputOneFileName, "wb")
outputWriterOne.write(outputStreamOne)
