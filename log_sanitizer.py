import re
import sys
from os import listdir
from os.path import isfile, isdir, basename
from magic import from_file

ignored_files=[]

def main():
	if len(sys.argv)!= 3:
		print '''
====================
Custom LOG Sanitizer
====================
Usage: python %s <log file> [OPTION]

OPTIONS AVAILABLE:
-i Clean IP Addresses
-h Clean HostNames
-a Clean All
''' % sys.argv[0]
		sys.exit(0)
	else:
		input=sys.argv[1]
		option=sys.argv[2]
		check_arg(input,option)


def check_arg(input,opt):
	if isfile(input) and from_file(input, mime=True)[:4]=='text':
		inputFile=open(input, 'r').readlines()
		out_filename=input + '.cln'
   		outFile=open(out_filename, 'w')
		if opt=='-i':
			for line in inputFile:
				outFile.write(clean_ip(line))
		if opt=='-h':
			for line in inputFile:
				outFile.write(clean_host(line))
		if opt=='-a':
			for line in inputFile:
				outFile.write(clean_both(line))
		
	elif isdir(input):
		for item in listdir(input):
			file_name=item.split('.')
			try:
				if file_name[-1]=='log' and from_file(item, mime=True)[:4]=='text':
					inputFile=open(item, 'r').readlines()
		                        out_filename=item+ '.cln'
                			outFile=open(out_filename, 'w')
					if opt=='-i':
                        			for line in inputFile:
                                			outFile.write(clean_ip(line))
                			if opt=='-h':
                        			for line in inputFile:
                                			outFile.write(clean_host(line))
					if opt=='-a':
		        	                for line in inputFile:
                	        		        outFile.write(clean_both(line))

			except IndexError:
				ignored_files.append(item)
					
def clean_ip(input):
	ip_pattn=re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	emp_val_ip=' xxx.xxx.xxx '
	return re.sub(ip_pattn,emp_val_ip,input)

def clean_host(input):
	host_pattn=re.compile(r'\[A-Z]+\|')
	emp_val_host='node '
	return re.sub(host_pattn,emp_val_host,input)

def clean_both(input):
	both_pattn=re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|[A-Z0-9]+\|')
	emp_val=' xxxxx '
	return re.sub(both_pattn,emp_val,input)

if __name__ == '__main__':
	main()
