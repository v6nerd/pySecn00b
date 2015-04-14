import sys
from urllib import unquote
import re
from binascii import unhexlify
from hashlib import md5

def main():
	if len(sys.argv)!=2:
		print "Usage: %s <file>" % sys.argv[0]
		sys.exit(0)
	else:
		inFile=open(sys.argv[1], 'r').readlines()
		url_hash_list=[]
		for line in inFile:
			curr_hash_val=line_hash(line)
			process_line=check_hash(curr_hash_val,url_hash_list)
			url_hash_list.append(curr_hash_val)
			if '%' in line and process_line==True:
				dec_line=url_decode(line)
				if '0x' in dec_line:
					print hex_lookup(dec_line)
				else:
					print dec_line
			if '0x' in line and process_line==True:
				print hex_lookup(line)
			

def check_hash(curr_val,list):
	if curr_val not in list:
		return True
	else:
		return False

def line_hash(input):
	hash_val=md5(input.encode())
	return hash_val.hexdigest()

def url_decode(input):
	url=unquote(input)
	return url.decode('utf-8', 'ignore')

def hex_lookup(input):
	hex_val=re.findall(r'0x(.*?),',input)
        return re.sub(r'0x(.*?),',hex_decode(hex_val[0]),input)

def hex_decode(input):
	if len(input) % 2 ==0:
		try:
                 uhex_val=unhexlify(input)
                 return uhex_val + ","
                except TypeError:
		 pass

if __name__ == '__main__':
	main()
