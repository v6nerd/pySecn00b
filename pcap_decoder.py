import sys
import re
from imp import load_source
load_source('urlDecoder','/root/pySecn00b/urlDecoder.py')
from urlDecoder import decode

url_hash_list=[]

def get_requests(line):
	xr_gurl=re.sub(r'^(.*)GET',"",line).strip(' ')
	host_info=get_host(line)
        return (re.sub(r'HTTP/1.1(.*)',"",xr_gurl).strip('\r\n'))

def post_requests(line):
	xr_purl=re.sub(r'^(.*)POST',"",line)
       	xl_purl=re.sub(r'HTTP/1.1(.*)',"",xr_purl).strip('\r\n')
        return xl_purl.strip(' ')

def cookie(line):
	return (re.sub(r'^(.*)ie:',"",line))

def user_agent(line):
	return (re.sub(r'(.*)gent:',"",line)).strip('\r\n')

def get_host(line):
	return (re.sub(r'^(.*)st:',"",line)).strip('\r\n')

def url_decode(input):
	check_request=decode()
        #curr_hash_val=check_request.line_hash(input)
        #process_line=check_request.check_hash(curr_hash_val,url_hash_list)
        #url_hash_list.append(curr_hash_val)
        if '%' in input:
		dec_line=check_request.url_decode(input)
		if '0x' in dec_line:
			return check_request.hex_lookup(dec_line)
                else:
			return dec_line
        if '0x' in input:
		return check_request.hex_lookup(input)

def url_sort(input):
	input_hash=decode()
	curr_hash_val=input_hash.line_hash(input)
        process_line=input_hash.check_hash(curr_hash_val,url_hash_list)
        url_hash_list.append(curr_hash_val)
	if process_line==True:
		print url_decode(input)

def line_ext(file,opt):
		host_info=''
		for line in file:
			if 'Host' in line:
				host_info=get_host(line)
			if 'GET' in line and opt=='-g':
				print (host_info + get_requests(line)).strip(' ')
				url_sort((host_info + get_requests(line)).strip(' '))
			if 'POST' in line and opt=='-p':
				url_sort((host_info + post_requests(line)).strip(' '))
			if 'User-Agent' in line and opt == '-u':
				print user_agent(line)
			if 'Cookie' in line and opt=='-c':
				print cookie(line)

def main():
	if len(sys.argv) < 3:
		print ("Usage:\n %s <pcap file> [OPTION]\n\n"+
              		"AVAILABLE OPTIONS:\n"+
              		" -p\tExtract HTTP POST\n"+
              		" -g\tExtract HTTP GET\n"+
			" -u\tExtract User-Agent Values\n"+
             		" -c\tExtract Cookie Values\n") % sys.argv[0]
	        sys.exit(0)
	else:
		inputFile=file(sys.argv[1], 'r').readlines()
		line_ext(inputFile, sys.argv[2])
			
if __name__ == '__main__':
	main()
