#!/bin/python

import pandas as pd
import numpy as np
import sys
import matplotlib as plot
import apachelog

if len(sys.argv)!=2:
	print "Usage: python apache_log_analysis.py <log file>"
	sys.exit(0)
else:
	apache_log=file(sys.argv[1], 'r').readlines()

#http_err=range(400,418,1)

#Example log line from the available log
ex_url_apache='134.251.87.133 - - [24/Dec/2014:01:00:10 +0800] "GET /IN/common/print.js HTTP/1.1" 200'
nformat_apache=r'%h %l %u %t \"%r\" %>s %b'

#ex_url_ISA='104.224.147.94 Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0) https://cards.rblbank.com:443/IN/ShowImage?linkid= 302'
#nformat_ISA=r'%h \"%{User-Agent}i\" %>s'

p=apachelog.parser(nformat_apache)
log_lst=[]

for line in apache_log:
	try:
	 data= p.parse(line)
	 log_lst.append(data['%t'] + " " + data['%b'] + " " + data['%r'] + " " + data['%>s'])

	except apachelog.ApacheLogParserError:
		sys.stderr.write('Unable to read line at %s' %line)

df=pd.DataFrame(log_lst)

'''
del df ['%h']
del df ['%l']
del df ['%u']
del df ['%b']
'''

df=df.rename(columns={'%t': 'Time', '%r': 'Requested URL', '%>s': 'Status'})

df.index=pd.to_datetime(df.pop('Time'))
print df[0:100]
