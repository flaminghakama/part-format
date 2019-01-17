
# make-insides.py input1.pdf input2.pdf output1.pdf rectoPageNumber1 rectoPageNumber2 

# Creates the inside pages of two different booklets, 
# each with half page meaning a file has four pages: 
# book 2 verso, book 1 recto, book 1 verso, book 2 recto

# rectoPageNumber1 is the page number of the first of the two pages from the first book, 
# and rectoPageNumber2 is the page number of the first of the two pages from the second book

import sys
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger

inputOneFileName = sys.argv[1] 
inputTwoFileName = sys.argv[2] 
outputOneFileName = sys.argv[3] 
rectoPageNumberOne = int(sys.argv[4])
versoPageNumberOne = rectoPageNumber + 1 
rectoPageNumberTwo = int(sys.argv[5])
versoPageNumberTwo = rectoPageNumber + 1 
print "input 1: " + inputOneFileName
print "input 2: " + inputTwoFileName 
print "output 1: " + outputOneFileName 
print "book 1 rector page number: " + rectoPageNumberOne
print "book 1 verso page number: " + versoPageNumberOne
print "book 2 recto page number: " + rectoPageNumberOne
print "book 2 verso page number: " + versoPageNumberOne

inputReaderOne = PdfFileReader(open(inputOneFileName, "rb"))
inputReaderTwo = PdfFileReader(open(inputTwoFileName, "rb"))
outputWriterOne = PdfFileWriter()

outputWriterOne.addPage(inputReaderTwo.getPage(versoPageNumberTwo))
outputWriterOne.addPage(inputReaderOne.getPage(rectoPageNumberOne))
outputWriterOne.addPage(inputReaderOne.getPage(versoPageNumberOne))
outputWriterOne.addPage(inputReaderTwo.getPage(rectoPageNumberTwo))

outputStreamOne = file(outputOneFileName, "wb")
outputWriterOne.write(outputStreamOne)
