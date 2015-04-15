import sys
from urllib import unquote
import re
from binascii import unhexlify
from hashlib import md5

class decode:

	def url_decode(self,input):
		url=unquote(input)
		return url.decode('utf-8', 'ignore')

	def hex_lookup(self,input):
		hex_val=re.findall(r'0x(.*?),',input)
        	return re.sub(r'0x(.*?),',self.hex_decode(hex_val[0]),input)

	def hex_decode(self,input):
		if len(input) % 2 ==0:
			try:
                 	 uhex_val=unhexlify(input)
                 	 return uhex_val + ","
	                except TypeError:
			 pass

class hash:		

	def check_hash(self,curr_val,list):
                if curr_val not in list:
                        return True
                else:
                        return False
	
	def line_hash(self,input):
		hash_val=md5(input.encode())
		return hash_val.hexdigest()



