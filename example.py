# example.py

import argparse
from datetime import datetime
import os.path
from PyPDF2 import PdfFileWriter, PdfFileReader

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

#  Define the valid page formats
validPageFormats = {
	'1': 'valid', 
	'1L': 'valid', 
	'1R': 'valid', 
	'2': 'valid', 
	'2L': 'valid', 
	'2R': 'valid', 
	'3': 'valid', 
	'4': 'valid',
	'5': 'valid', 
	'5L': 'valid', 
	'5R': 'valid', 
	'6': 'valid',
	'6L': 'valid',
	'6R': 'valid', 
	'7': 'valid', 
	'8': 'valid', 
	'9': 'valid',
	'9L': 'valid', 
	'9R': 'valid', 
	'10': 'valid', 
	'10L': 'valid', 
	'10R': 'valid', 
	'11': 'valid', 
	'12': 'valid'
}

#  Count the number of pages in a file
def getNumberOfPages(file):
	fileReader = PdfFileReader(open(file, "rb"))
	return str(fileReader.getNumPages())

#  Determine the order of pages
outsidePages = []
insidePages = [] 
def enqueuePages(file, layoutFormat):
	return 'no enqueuing going on yet' 

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
				print "ignoring layout format " + arg + " because no files have been specified"
		else:
			print 'argument was neither file nor layout format: ' + arg

#  Gather pages in the right orders
if len(files) > 0:
	for file in files:
		if layoutFormat[file] == 'default':
			layoutFormat[file] = getNumberOfPages(file)
		print "file " + file + " has format " + layoutFormat[file]
		# enqueuePages(file, layoutFormat[file])
else:
	print "No files specified"
