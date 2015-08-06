import pyshark
import sys

pcap_file=pyshark.FileCapture(sys.argv[1])

for item in pcap_file:
	try:
		payload_data=str(item.layers[5]).split(":")
		payload=payload_data[1].strip()
	except IndexError:
		pass
