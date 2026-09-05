#!/usr/bin/env python3
import argparse
import sys

def parse_args():
    parser = argparse.ArgumentParser(
        add_help=False,
        color=False
    )
    
    parser.add_argument("-t", "--target", required=True, help="Define the target IP")
    parser.add_argument("-p", "--portscan", required=False, choices=["nmap", "masscan"], default="Not Defined")
    parser.add_argument("-d", "--webdisc", required=False, choices=["ffuf", "gobuster", "dirbuster"], default="Not Defined")
    parser.add_argument("-w", "--webenum", required=False, choices=["whatweb", "wappalyzer", "nikto"], default="Not Defined")
    return parser.parse_args()

def main():
    if len(sys.argv) == 1:
        print("""
Enumizer - a quick network and web enumeration toolkit using multiple popular tools.

Usage:
    ./main.py -t <target-ip> [options]
    or
    python3 main.py -t <taget-ip> [options]

To be able to use the script properly you need to specify the tools (available tools are given below). 

Options:
    -t, --target        Target IP address (required)
    -p, --portscan      Define the port scanning tool
    -d, --web-disc      Define the web discovery tool
    -w, --web-enum      Define the web enumeration tool

Available tools:
    Port scanning - nmap, masscan
    Web discovery - ffuf, gobuster, dirbuster
    Web enumeration - whatweb, wappalyzer, nikto (may work extremely slow.)

Example usage:
    ./main.py -t 10.10.10.10 -p nmap -d ffuf -w nikto

Disclaimer - This is an open source tool for real pentesting usage, we do not hold any accountability
             for any damage caused, that responsibility is on you.
        """)
        return


    args = parse_args()
    print(fr"""                                                       
        ,------.                          ,--.                      
        |  .---',--,--, ,--.,--.,--,--,--.`--',-----. ,---. ,--.--. 
        |  `--, |      \|  ||  ||        |,--.`-.  / | .-. :|  .--' 
        |  `---.|  ||  |'  ''  '|  |  |  ||  | /  `-.\   --.|  |    
        `------'`--''--' `----' `--`--`--'`--'`-----' `----'`--'    

        -------------------------------------------------------------------------------------
        [+] Performing attack on {args.target}...
    """)

            
    

if __name__=="__main__":
    main()