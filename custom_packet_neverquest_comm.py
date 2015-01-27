#SCAPY NeverQuest Packet Manipulation

import random
from scapy.all import *

random_sp=random.randint(1024,65535)

i=IP(version=4, dst="107.155.108.17", ttl=63, ihl=20, len=69)
ack=TCP(sport=random_sp, dport=22, flags="S", seq=1, window=1460, options=[('NOP',None),('NOP', None)])
sr1(i/ack)
