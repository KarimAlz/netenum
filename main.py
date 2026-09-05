#!/usr/bin/env python3
import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        prog="enumizer",
        description="Enumizer - quick network, web enumeration and analyzer tool."
    )

    parser.add_argument("-t", "--target", required=True, help="Define the target IP")
    parser.add_argument("-p", "--portscan", required=False, help="Define the port scanning tool", choices=["nmap", "masscan"], default="nmap")
    parser.add_argument("-d", "--webdisc", required=False, help="Define the web discovery tools (directory bruteforce, dns enum)", choices=["ffuf", "gobuster", "dirbuster"], default="ffuf")
    parser.add_argument("-w", "--webenum", required=False, help="Define the web enumeration tool", choices=["whatweb", "wappalyzer"], default="whatweb")
    return parser.parse_args()

def main():
    args = parse_args()
    print(fr"""                                                       
        ,------.                          ,--.                      
        |  .---',--,--, ,--.,--.,--,--,--.`--',-----. ,---. ,--.--. 
        |  `--, |      \|  ||  ||        |,--.`-.  / | .-. :|  .--' 
        |  `---.|  ||  |'  ''  '|  |  |  ||  | /  `-.\   --.|  |    
        `------'`--''--' `----' `--`--`--'`--'`-----' `----'`--'    

        -------------------------------------------------------------------------------------
        [+] Performing attack on {args.target}...
        [*] Port scan tool: {args.portscan}
        [*] Web discovery tool: {args.webdisc}
        [*] Web enumeration tool: {args.webenum}
        Done.
    """)
            
    

if __name__=="__main__":
    main()