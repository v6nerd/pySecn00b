import sys
import re
from imp import load_source
load_source('urlDecoder','./urlDecoder.py')
from urlDecoder import decode, hash

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
	x=decode()
        if '%' in input:
		dec_line=x.url_decode(input)
		if '0x' in dec_line:
			return x.hex_lookup(dec_line)
                else:
			return dec_line
        if '0x' in input:
		return x.hex_lookup(input)

def url_sort(input,dflag):
	x=hash()
	curr_hash_val=x.line_hash(input)
        process_line=x.check_hash(curr_hash_val,url_hash_list)
        url_hash_list.append(curr_hash_val)
	if process_line==True and dflag==1:
		print url_decode(input)
	elif process_line==True and dflag==0:
		print input

def url_ext(file,opt,dflag=0):
		host_info=''
		for line in file:
			if 'Host' in line:
				host_info=get_host(line)
			if 'GET' in line and opt=='-g':
				url_sort((host_info + get_requests(line)).strip(' '),dflag)
			if 'POST' in line and opt=='-p':
				url_sort((host_info + post_requests(line)).strip(' '),dflag)
			if 'User-Agent' in line and opt == '-u':
				print user_agent(line)
			if 'Cookie' in line and opt=='-c':
				print cookie(line)

def main():
	if len(sys.argv) < 3:
		print ("Usage:\n %s <pcap file> [OPTION]\n\n"+
              		"AVAILABLE OPTIONS:\n"+
              		" -p\t\tExtract HTTP POST\n"+
              		" -g\t\tExtract HTTP GET\n"+
			" -u\t\tExtract User-Agent Values\n"+
             		" -c\t\tExtract Cookie Values\n"+
			" +decode \tDecode GET/POST Requests\n" ) % sys.argv[0]
	        sys.exit(0)
	elif len(sys.argv)==3:
		inputFile=file(sys.argv[1], 'r').readlines()
		url_ext(inputFile, sys.argv[2])
	elif len(sys.argv)==4 and sys.argv[3]=='+decode':
		inputFile=file(sys.argv[1], 'r').readlines()
                url_ext(inputFile, sys.argv[2],1)

			
if __name__ == '__main__':
	main()
