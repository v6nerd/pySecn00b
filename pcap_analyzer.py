#**********************
# Simple PCAP Analyzer
#**********************

import sys
from pcapy import open_offline
#from pcapy import open_offline.Process
from impacket.ImpactDecoder import EthDecoder
from impacket.ImpactPacket import IP, TCP, UDP, ICMP

if len(sys.argv)!=2:
	print "Usage:python pcap_analyzer.py <pcap file>"
	sys.exit(0)

pcap_file=file(sys.argv[1], 'read')
#pcap_file="/root/shared/failed_attempts_HPTW_041114.pcap"

packetReader=open_offline(pcap_file)
packetReader.loop(0,Process)

def process(header,data):
	pcap_decode=ImpactDecoder.EthDecoder()
	ether_frame=pcap_decoder.decode(data)
	ip_header=ether.child()
	packet_type=ipheader.child().protocol
	print packet_type
	
	'''
	if packet_type==6:
		tcp_header=ip_header.child()
	if (tcp_header.get_PSH() and tcp_header.get_ACK()) and \
	   (tcp_header.get
	'''
