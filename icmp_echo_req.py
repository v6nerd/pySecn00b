import random
from scapy.all import *

src_port=random.randint(1024,65535)
ping=IP(dst="192.168.30.168")/ICMP()
sr1(ping)
