#!/bin/python

import re
import sys

if len(sys.argv)!=2:
	print "Usage: python extract_urls.py <input file>"
	sys.exit(0)
else:
	input=sys.argv[1]

inFile=file(input,'r').readlines()

for line in inFile:
	urls=re.findall(r'(GET|POST) /+',line)
	print urls




