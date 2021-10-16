#!/usr/bin/env python3
import socket
import re

ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
port_min = 0
port_max = 65535

print("""
      __  __                      ___              ______                                
     / / / /___  __  ____________/   |  ____  ____/ / __ \________  ____ _____ ___  _____
    / /_/ / __ \/ / / / ___/ ___/ /| | / __ \/ __  / / / / ___/ _ \/ __ `/ __ `__ \/ ___/
   / __  / /_/ / /_/ / /  (__  ) ___ |/ / / / /_/ / /_/ / /  /  __/ /_/ / / / / / (__  ) 
  /_/ /_/\____/\__,_/_/  /____/_/  |_/_/ /_/\__,_/_____/_/   \___/\__,_/_/ /_/ /_/____/  """)

open_ports = []

while True:
    ip_add_entered = input("\nEnter the ip address that you want to scan: ")
    if ip_add_pattern.search(ip_add_entered):
        print(f"{ip_add_entered} is a valid ip address")
        break

while True:
    print("Please enter the range of ports you want to scan in format: <int>-<int> (ex would be 20-80)")
    port_range = input("Enter port range: ")
    port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break

for port in range(port_min, port_max + 1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            s.connect((ip_add_entered, port))
            open_ports.append(port)

    except:
        pass

for port in open_ports:
    print(f"Port {port} is open on {ip_add_entered}.")