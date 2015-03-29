#!/bin/python

import sys

if len(sys.argv)!=2:
	print "Usage: utf_decode.py file"
	sys.exit(0)

inFile=file(sys.argv[1],'r').readlines()

for line in inFile:
	u=unicode(line, 'unicode-escape')
	print u.decode('utf-8')

