#!/bin/python

import sys

if len(sys.argv)!=2:
	print "USAGE:command datafile"
	sys.exit(0)

data=file(sys.argv[1], 'r').readlines()

for ip in data:
	if "$10" in ip:
		print ip
