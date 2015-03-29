import re
source_file=open('/root/semtex0.dump', 'r').readlines()
target_file=file('/root/semtex0.out','rw+')

for line in source_file:
	val=[]
	xl=re.sub(r'^(.*): ',"", line);
	xr=re.sub(r'  (.*)', "", xl);
	s2_byte=re.findall(r'\w{2}', xr);
	for id, byte in enumerate(s2_byte):
		if id % 2 == 0:
			val.append(s2_byte[id]);
				
			
