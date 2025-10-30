import json
import shutil
import sys

try:
    import nmap  # python-nmap wrapper
except ImportError:
    print("Missing python library 'python-nmap'. Install with: pip install python-nmap")
    sys.exit(1)

def run_network_scan(target_range):

    # Check nmap executable exists
    if shutil.which("nmap") is None:
        raise RuntimeError("nmap executable not found. Install Nmap and ensure it's on your PATH.")

    nm = nmap.PortScanner()
     # Use -sn (host discovery only) and -n (skip DNS) for speed and simplicity
    nm.scan(hosts=target_range, arguments='-sn -n')

    all_live_hosts = []

    for host in nm.all_hosts():

        host_name = nm[host].hostname()
        host_state = nm[host].state()

        port_data = []


        for proto in nm[host].all_protocols():

             lport = nm[host][proto].keys()
             for port in lport:
                  port_detail = {
                    "protocol": proto,
                    "port_no": port,
                    "port_state": nm[host][proto][port]["state"],
                    # Optional: Add service info
                    "service": nm[host][proto][port]["name"]
                }
                  port_data.append(port_detail)
                  
        
        live_host = {
            "ip": host,
            "host_name": host_name,
            "state": host_state,
            "open_ports": port_data
        }

        all_live_hosts.append(live_host)

    with open('live_hosts.json', 'w') as file:
            json.dump(all_live_hosts, file, indent=4)

    print(f"\nScan complete. Found {len(all_live_hosts)} live host(s).")
    print(f"Report saved to: live_hosts.json")


if __name__ == '__main__':
    try:
        run_network_scan('192.168.0.0/24')
    except KeyboardInterrupt as e:
         print("\nNetwork Scan stopped by user.....")
    except Exception as e:
         print(f"\nAn unexpected error occurred: {e}")
         sys.exit(1)
