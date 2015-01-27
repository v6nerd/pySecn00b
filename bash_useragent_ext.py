import sys
import re

if len(sys.argv)!=2:
        print "Usage: user_agent_ext.py file"
        sys.exit(0)

InFile=file(sys.argv[1], 'r').readlines()

for line in InFile:
	if "User-Agent" in line:
		output=re.sub(r'^(.*)t:',"",line)
		print output

