
# make-inside.py input1.pdf output1.pdf rectoPageNumber 

# Creates the inside page of a booklet with a half page,
# Meaning a file has three pages: empty, recto, verso

# rectoPageNumber is the page number of the first of the two pages, 

import sys
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger

inputOneFileName = sys.argv[1] 
outputOneFileName = sys.argv[2] 
rectoPageNumber = int(sys.argv[3])
versoPageNumber = rectoPageNumber + 1 
print "input 1: " + inputOneFileName
print "output 1: " + outputOneFileName 
print "recto page number: " + rectoPageNumber
print "verso page number: " + versoPageNumber

inputReaderOne = PdfFileReader(open(inputOneFileName, "rb"))
outputWriterOne = PdfFileWriter()

outputWriterOne.addPage(inputReaderOne.getPage(rectoPageNumber))
outputWriterOne.addPage(inputReaderOne.getPage(versoPageNumber))
outputWriterOne.insertBlankPage()
outputStreamOne = file(outputOneFileName, "wb")
outputWriterOne.write(outputStreamOne)
