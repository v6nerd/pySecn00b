import sys
import re

if len(sys.argv)<3:
        print ("Usage:\nhttp_request_ext.py file [OPTION]\n\n"+
	      "AVAILABLE OPTIONS:\n"+ 
	      "	-p\tCollect HTTP POST Requests\n"+
	      "	-g\tCollect HTTP GET Requests\n"+
	      "	-c\tCollect Cookie Values\n"+
	      "	+h\tInclude HOST Address\n")
	
        sys.exit(0)

InFile=file(sys.argv[1], 'r').readlines()

def get_requests(self):
	for line in self:
		if "GET" in line:
                	xr_gurl=re.sub(r'^(.*)GET',"",line).strip(' ')
                	xl_gurl=re.sub(r'HTTP/1.1(.*)',"",xr_gurl).strip('\r\n')
        	        print xl_gurl

def post_requests(self):
	for line in self:
		if "POST" in line:
			xr_purl=re.sub(r'^(.*)POST',"",line)
        	        xl_purl=re.sub(r'HTTP/1.1(.*)',"",xr_purl).strip('\r\n')
                	print xl_purl.strip(' ')

def cookies(self):
	for line in self:
		if "Cookie" in line:
			xr_cookie=re.sub(r'^(.*)ie:',"",line)
			print xr_cookie

def get_host(self):
	for line in self:
		if "Host" in line:
			xr_host=re.sub(r'^(.*)st:',"",line)
                	#xl_host=re.sub(r'(.*)',"",xr_host).strip('\r\n')
			print line

def get_uni_host_ip(self):
		for line in self:
			ip_pattn=re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
			ip_addr=re.findall(ip_pattn, line)
			ip_addr_uni=[]
			print ip_addr.index

			#if ip_addr.index > 0 and ip_addr.index != ip_addr_uni.index -1:
			#	ip_addr_uni.append(ip_addr)
			#	print ip_addr_uni
	
		
if sys.argv[2]=="-p":
	post_requests(InFile)
	sys.exit(0)

elif sys.argv[2]=="-g":
	get_requests(InFile)
	sys.exit(0)

elif sys.argv[2]=="-c":
        cookies(InFile)
        sys.exit(0)

'''
elif sys.argv[3]=="+h":
	get_host(InFile)
	sys.exit(0)
'''

if sys.argv[2]=="+ip":
	get_uni_host_ip(InFile)
	sys.exit(0)
