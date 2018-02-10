# rightify-3page.py

# combine-1stPage-3rdPage.py input1.pdf input2.pdf output.pdf

import sys
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger

inputFileOneName = sys.argv[1] 
inputFileTwoName = sys.argv[2] 
outputFileName = sys.argv[3] 
print "input 1: " + inputFileOneName 
print "input 2: " + inputFileTwoName 
print "output: " + outputFileName 

inputReaderOne = PdfFileReader(open(inputFileOneName, "rb"))
inputReaderTwo = PdfFileReader(open(inputFileTwoName, "rb"))
outputWriter = PdfFileWriter()

outputWriter.addPage(inputReaderOne.getPage(0))
outputWriter.addPage(inputReaderTwo.getPage(2))
outputStream = file(outputFileName, "wb")
outputWriter.write(outputStream)
