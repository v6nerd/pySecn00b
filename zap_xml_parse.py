from xml.dom.minidom import parse
import xml.dom.minidom
import sys
import csv

#uni_file=open(sys.argv[1],'r')
#non_uni_file=uni_file.decode("utf8")
dom_tree=parse(sys.argv[1])
collect=dom_tree.documentElement
output_data=[[],[],[],[],[],[],[],[]]
out_filename=((sys.argv[1].split("/")[-1]).split(".")[0])+".csv"
out_file=open(out_filename,'w')
write_csv=csv.writer(out_file, dialect=csv.excel)


for item in  collect.getElementsByTagName("alertitem"):
	try:
		risk_desc=item.getElementsByTagName('riskdesc')[0]
		output_data[0].append(risk_desc.childNodes[0].data)

	except IndexError:
		output_data[0].append("NONE")

			
	try:
		alert_name=item.getElementsByTagName('alert')[0]
		output_data[1].append(alert_name.childNodes[0].data)

	except IndexError:
		output_data[1].append("NONE")

	
	try:
		alert_desc=item.getElementsByTagName('desc')[0]
		output_data[2].append((alert_desc.childNodes[0].data).encode("utf-8"))

	except IndexError:
		output_data[2].append("NONE")

	
	try:
		alert_solution=item.getElementsByTagName('solution')[0]
		output_data[3].append((alert_solution.childNodes[0].data).encode("utf-8"))

	except IndexError:
		output_data[3].append("NONE")

	
	try:
		alert_ref=item.getElementsByTagName('reference')[0]
		output_data[4].append((alert_ref.childNodes[0].data).encode("utf-8"))

	except IndexError:
        	output_data[4].append("NONE")

	try:
		uri=item.getElementsByTagName('uri')[0]
		output_data[5].append(uri.childNodes[0].data)

	except IndexError:
      		output_data[5].append("NONE")

	try:
		evid=item.getElementsByTagName('evidence')[0]
		output_data[6].append(evid.childNodes[0].data)

	except IndexError:
		output_data[6].append("NONE")


	try:
		attack=item.getElementsByTagName('attack')[0]
		output_data[7].append(attack.childNodes[0].data)

	except IndexError:
		output_data[7].append("NONE")

try:
 for i in range(0,len(output_data[0])-1):	
	row=[]
	for x in range(0,len(output_data)):
	 	row.append(str(output_data[x][i]).replace(',',';c'))
	print row

except UnicodeEncodeError:
 raise

#print output_data
#	for x in xrange(0,len(output_data)-1):
#		print output_data[x][i]

#write_csv.writerows(output_data)
