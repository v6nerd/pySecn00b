import re
import sys
from os import listdir
from os.path import isfile, isdir, basename
from magic import from_file

#input=sys.argv[1]
ignored_files=[]

def main():
	if len(sys.argv)!= 2:
		print '== Custom LOG Sanitizer ==\r\n'
		print 'Usage: python %s <log file>\r\n' % sys.argv[0]
		sys.exit(0)
	else:
		input=sys.argv[1]
		check_arg(input)

def check_arg(input):
	if isfile(input) and from_file(input, mime=True)[:4]=='text':
		clean_logs(input)
	elif isdir(input):
		for item in listdir(input):
			file_name=item.split('.')
			try:
				if file_name[-1]=='log' and from_file(item, mime=True)[:4]=='text':
					clean_logs(item)
			except IndexError:
				ignored_files.append(item)
					

def clean_logs(file):
	inputFile=open(file, 'r').readlines()
	out_filename=file + '.cln'
	outFile=open(out_filename, 'w')
	s_ip_pattn=re.compile('\[\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\]')
	m_ip_pattn=re.compile('\[\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(.*)\]')
	emp_val='[xxx.xxx.xxx.xxx]'
	for line in inputFile:
		s_ip_sub=re.sub(s_ip_pattn,emp_val,line)
		m_ip_sub=re.sub(m_ip_pattn,emp_val,s_ip_sub)
		outFile.write(m_ip_sub)

if __name__ == '__main__':
	main()
