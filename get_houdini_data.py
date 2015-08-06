import sys
import re
from scapy.all import *

pcap=rdpcap(sys.argv[1])
ip_lst=[]
ua=[]

for packet in pcap:
	if packet[IP].src !="" and packet.haslayer(Raw):
		try: 
			ip=packet[IP].src	
			ua_raw=re.findall(r'User-Agent: ?(.*\<\|\>)', str(packet[Raw]))[0]
			ua_cln=re.sub(r'\<\|\>', " ", ua_raw)
			print ip + " " + ua_cln
		except IndexError:
			pass 
	
