# example.py

import argparse
from datetime import datetime
import os.path

#  Parse the command line

parser = argparse.ArgumentParser(description='Process file and layout format specifications')
parser.add_argument('-o','--outputFilePrefix', help='Prefix for output files')
parser.add_argument("input", nargs='+')
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

#  Evaluate the file and format specs
for arg in args.input:
    if os.path.isfile(arg):
        print "    Argument " + arg + " is a file"
    else:
        print "    Argument " + arg + " is NOT a file"