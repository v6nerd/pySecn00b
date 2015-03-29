#**************************
# McAfee NSM URL Extractor
#**************************

import re
import os
import hashlib
import imp
from socket import error as sockerr
import errno
from urllib2 import URLError, HTTPError, urlopen, Request 
from httplib import BadStatusLine
from optparse import OptionParser
wepawet=imp.load_source('wepawet','/root/pySecn00b/wepawet_check_nsm.py')

options=OptionParser(usage='%prog [options]', description='Parse URLs from McAfeeNSM Console RAW Data')
options.set_usage("McAfeeNSM_URL_Parser.py -s <sourcefile>")
options.add_option("-s", "--source-file", type="string", action="store", dest="filename", help="locate the SourceFile to be parsed [required]")
options.add_option("-e", "--file-extension", type="string", action="store", dest="filetype", default=".js", help="define file extension [default=%default]" )
#options.add_option("-c", "--check-response", type="int", action="store", dest="verify",default=1)
opts, args = options.parse_args()
sourcefile=str(opts.filename) 
ext=str(opts.filetype)
#response_check=opts.verify
targetfile_name=(sourcefile.split('/')[-1]).split('.')[0] + "_URLs"
hashfile_name=(targetfile_name.strip('_URLs') + "_hash")
targetfile=file(targetfile_name, 'w')
hashfile=file(hashfile_name, 'w')

def input_check():
	if sourcefile=="None":
		return options.print_help();
	else:
		main()
		#url_query()

def grep_urls(inDATA):
	ip_pattern=re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
        src_ip=re.findall(ip_pattern, inDATA)
   	xl=re.sub(r'^(.*)HTTP URI == ',"",inDATA);
        xr=re.sub(r';(.*)',"",xl);
	if "n/a" not in xr:
		return "http://" + src_ip[0] + xr
	
def main():
	if os.path.exists(sourcefile):
		raw_data=open(sourcefile, 'r').readlines();
		for line in raw_data:
			if "HTTP URI" in line:
				refined_data=grep_urls(line)
				targetfile.write(refined_data)
				query=http_response_check(refined_data)
				if "None" in str(query) and ext in refined_data:
					http_fetch(refined_data)
					#url_submit(refined_data)
					#url_query()
					#hash_file=filename_gen(refined_data)
					#hash_value=hash_gen(hash_file)
					#url_query(hashfile_name)
												
	else:
		print "File Not Found!"


def http_response_check(url):
	http_parse=Request(url)
	try:
	    urlopen(http_parse)
	except URLError as error:		
		return error.reason
	except HTTPError as  error:
		return error.reason
	except sockerr as error:
		if error.errno == errno.ECONNRESET:
			pass
	except BadStatusLine as error:  
		return error

def filename_gen(url):
         scriptfile_name=(url.split('/')[-1]).strip('\n')
         return str(scriptfile_name)
		
def http_fetch(url):
        scriptfile_name=(url.split('/')[-1]).strip('\n')
	js_read=urlopen(url).read()
	script_file=file(scriptfile_name, 'w')
	return script_file.write(js_read)

def hash_gen(inFile):
	with open(inFile, 'r') as file:
		sha1_hash_gen=hashlib.sha1()
		buf=file.read(8192)
		while len(buf)> 0:
			sha1_hash_gen.update(buf)
			buf=file.read(8192)
		return sha1_hash_gen.hexdigest()

def url_submit(url):
	wepawet_submit=wepawet.wepawet_submit(url)
	wepawet_hash=re.findall(r'>(.*)<', wepawet_submit)
	hashfile.write(wepawet_hash[0] + '\n')
	#print wepawet_hash[0] + ' >> wepawet hashcode generated'
	#print wepawet_hash[0]
	#if len(wepawet_hash[0]) == 32:
		#wepawet_result=wepawet.wepawet_query(wepawet_hash[0])
		#print wepawet_result

def url_query(inFile):
	with open(inFile, 'r') as hash_codes:
		for line in hash_codes:
			print line
			query=wepawet.wepawet_query(line)
			print query

input_check()
