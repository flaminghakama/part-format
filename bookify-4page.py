# bookify-4page.py

# bookify-4page.py input.pdf output.pdf

import sys
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger

inputFileName = sys.argv[1] 
outputFileName = sys.argv[2] 
print "input: " + inputFileName 
print "output: " + outputFileName 

inputReader = PdfFileReader(open(inputFileName, "rb"))
outputWriter = PdfFileWriter()

outputWriter.addPage(inputReader.getPage(3))
outputWriter.addPage(inputReader.getPage(0))
outputWriter.addPage(inputReader.getPage(1))
outputWriter.addPage(inputReader.getPage(2))
outputStream = file(outputFileName, "wb")
outputWriter.write(outputStream)
