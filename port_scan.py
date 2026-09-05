#!/usr/bin/env python3
import subprocess
import sys
import os
import xml.etree.ElementTree as ET

def parse_nmap_XML(path_to_xml):
    tree = ET.parse(path_to_xml)
    root = tree.getroot()

    open_ports = []

    for host in root.findall("host"):
        ip_address = host.find("address").get("addr")

        ports_section = host.find("ports")
        if ports_section is not None:
            for port in ports_section.findall("port"):
                port_state = port.find("state").get("state")
                
                if port_state == "open":
                    portid = port.get("portid")
                    protocol = port.get("protocol")

                    service = port.find("service")
                    service_name = service.get("name") if service is not None else "unknown"

                    open_ports.append({
                        "ip": ip_address,
                        "port": portid, 
                        "protocol": protocol, 
                        "service": service_name
                    })
        
    return open_ports


def run_nmap(target, mode="stealth", ports="default"):
    if mode == "stealth":
        command = ["nmap", "-sS", target, "-oA", "reports/port_scan"]
    os.makedirs("reports", exist_ok=True)
    print(f"[*] Running port scan: {' '.join(command)} ...")
    try:
        scan = subprocess.run(command, capture_output=True, text=True, check=True)
        print("[+] Scan completed!")
        print("-----NMAP SCAN REPORT-----")
        report = parse_nmap_XML("reports/port_scan.xml")
        for i in report:
            port_and_service = f"{i["port"]}/{i["service"]}"
            print(f"{port_and_service:<15} port ({i["protocol"]}) is open on host {i["ip"]}")
        print("\nThe reports are saved in /reports directory.")
    except subprocess.CalledProcessError as e:
        print(f"[-] Scan failed with exit code {e.returncode}")
        print(f"Error Details:\n{e.stderr}")


run_nmap("127.0.0.1", "stealth", "b")