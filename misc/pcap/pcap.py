import os
import pcapy as p
from scapy.all import *
a = " "
os.system("tshark  -T fields  -e frame.time -e  data.data -w Eavesdrop_Data.pcap > Eavesdrop_Data.txt -F pcap -c 1000")

data = "Eavesdrop_Data.pcap"
a = rdpcap(data)
