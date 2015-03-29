#!/usr/bin

import sys
import urllib
#import base64

if len(sys.argv)!=2:
	print "Usage: url_decode.py file"
	sys.exit(0)

inFile=file(sys.argv[1], 'r').readlines()

for line in inFile:
	url=urllib.unquote(line)
	url_decode=url.decode('utf-8', 'ignore')
	print url_decode
