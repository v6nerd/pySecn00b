#!/usr/bin

import sys
from urllib import unquote
import re
from binascii import unhexlify

def main():

	if len(sys.argv)!=2:
		print "Usage: %s <file>" % sys.argv[0]
		sys.exit(0)
	else:
		inFile=open(sys.argv[1], 'r').readlines()
		for line in inFile:
			decoded_url=url_decode(line)
			if '0x' in decoded_url:
				hex_val=re.findall(r'0x(.*?),',decoded_url)
				print re.sub(r'0x(.*?),',hex_decode(hex_val[0]),decoded_url)
			else:
				print decoded_url

def url_decode(input):
	url=unquote(input)
	return url.decode('utf-8', 'ignore')

def hex_decode(input):
	if len(input) % 2 ==0:
		try:
                 uhex_val=unhexlify(input)
                 return uhex_val + ","
                except TypeError:
		 pass

if __name__ == '__main__':
	main()
