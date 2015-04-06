import sys
import re

def get_requests(line):
	xr_gurl=re.sub(r'^(.*)GET',"",line).strip(' ')
	host_info=get_host(line)
        return (re.sub(r'HTTP/1.1(.*)',"",xr_gurl).strip('\r\n'))

def post_requests(line):
	xr_purl=re.sub(r'^(.*)POST',"",line)
       	xl_purl=re.sub(r'HTTP/1.1(.*)',"",xr_purl).strip('\r\n')
        return xl_purl.strip(' ')

def cookie(line):
	xr_cookie=re.sub(r'^(.*)ie:',"",line)
	print xr_cookie

def get_host(line):
	return (re.sub(r'^(.*)st:',"",line)).strip('\r\n')

def line_ext(file,opt):
		host_info=''
		for line in file:
			if 'Host' in line:
				host_info=get_host(line)
			elif 'GET' in line and opt=='-g':
				print (host_info + get_requests(line)).strip(' ')
			elif 'POST' in line and opt=='-g':
				print (host_info + post_requests(line)).strip(' ')
			elif 'User-Agent' in line and opt == '-u':
				print user-agent(line)
			elif 'Cookie' in line and opt=='-c':
				print cookie(line)

def main():
	if len(sys.argv) < 3:
		print ("Usage:\nhttp_request_ext.py file [OPTION]\n\n"+
              		"AVAILABLE OPTIONS:\n"+
              		" -p\tExtract HTTP POST\n"+
              		" -g\tExtract HTTP GET\n"+
             		" -c\tExtract Cookie Values\n")
	        sys.exit(0)
	else:
		inputFile=file(sys.argv[1], 'r').readlines()
		line_ext(inputFile, sys.argv[2])
			
if __name__ == '__main__':
	main()
