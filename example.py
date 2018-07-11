# example.py

import argparse
from datetime import datetime
import os.path
from PyPDF2 import PdfFileWriter, PdfFileReader
import layoutFormats

#  Parse the command line
parser = argparse.ArgumentParser(description='Process file and layout format specifications')
parser.add_argument('-o','--outputFilePrefix', help='Prefix for output layoutFormat (outside, inside)')
parser.add_argument('input', nargs='+')
args = parser.parse_args()

#  Determine the output file prefix 
now = datetime.now()
defaultOutputFilePrefix = now.strftime("%Y.%m.%d-%H:%M:%S-")
if args.outputFilePrefix:
    outputFilePrefix = args.outputFilePrefix
    print "Output file prefix specified: " + outputFilePrefix
else:
    outputFilePrefix = defaultOutputFilePrefix
    print "Using default output file prefix:" + outputFilePrefix

#  Count the number of pages in a file
def getNumberOfPages(file):
	fileReader = PdfFileReader(open(file, "rb"))
	return str(fileReader.getNumPages())

#  Evaluate the file and format specs
thisFile = 'no file specified'
files = []
layoutFormat = {}
for arg in args.input:
    if os.path.isfile(arg):
        thisFile = arg
        files.append(thisFile)
        layoutFormat[thisFile] = 'default'
    else:
		if validPageFormats.get(arg) == 'valid':
			if thisFile != 'no file specified':
				layoutFormat[thisFile] = arg
			else:
				print 'ignoring layout format ' + arg + ' because no files have been specified'
		else:
			print 'argument was neither file nor layout format: ' + arg


def isSideSpecified(format):
	return 'L' in format || 'R' in format


#  Gather pages in the right orders
outsidePages = []
insidePages = [] 
outsideCompositePages = []
insideCompositePages = []
nextHalfPageSide = 'L'
def enqueuePages(file, layoutFormat):

	#  Determine the page sequence 

	if ( validPageFormats.get(layoutFormat) == 'half' ) && isSideSpecified(layoutFormat):
		#  Do something with the already-specified half page
	else:
		if validPageFormats.get(layoutFormat) == 'determine side':
			if nextHalfPageSide == 'L': 
				layoutFormat = layoutFormat + 'L' 
				nextHalfPageSide = 'R'
			else:
				layoutFormat = layoutFormat + 'R'
				nextHalfPageSide = 'L' 


if len(files) > 0:
	for file in files:
		if layoutFormat[file] == 'default':
			layoutFormat[file] = getNumberOfPages(file)
		print 'file ' + file + ' has format ' + layoutFormat[file]
		# enqueuePages(file, layoutFormat[file])
else:
	print "No files specified"

#  Perpare output
def showContents(file):
	print 'No showing going on yet'

