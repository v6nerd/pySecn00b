#!/bin/python

import pandas as pd
import numpy as np
import sys
import matplotlib as plot
import apachelog

apache_log=file('/root/shared/tw_logs_241214/apache_access.txt', 'r').readlines()
http_err=range(400,418,1)

#ex_url='134.251.87.133 - - [24/Dec/2014:01:00:10 +0800] "GET /IN/common/print.js HTTP/1.1" 200'
nformat=r'%h %l %u %t \"%r\" %>s %b'
p=apachelog.parser(nformat)
log=[]

for line in apache_log:
	data= p.parse(line)
	for i in http_err:
		if str(i) in data['%>s']:
			  log.append(data['%t'] + " " + data['%>s'] + " " + data['%r'])
		 
df=pd.DataFrame(log)
df_out=df[0:100]

	#if data ['%>s'] in http_err:
	#	print data['%t'] + " " + data['%r']
	#print (data ['%t'] + " " + data['%>s'] + " " + data['%r'])
