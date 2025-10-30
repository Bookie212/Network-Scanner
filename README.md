Beginner Network Host Discovery

A minimal, beginner-friendly Python script that performs host discovery using Nmap (-sn) and saves the list of discovered hosts to live_hosts.json.

Features

1️⃣ Uses Nmap's host discovery (-sn) — no port scanning.

2️⃣ Simple, readable code for learning and quick usage.

3️⃣ Saves results to a JSON file with timestamp and basic host info (IP, hostname, state).

Requirements

1️⃣ Python 3.7+

2️⃣ Nmap executable installed and on your system PATH.

#️⃣ Windows: Download installer from https://nmap.org/
 or use Chocolatey:

  choco install nmap


#️⃣ Linux (Debian/Ubuntu):

  sudo apt update && sudo apt install nmap


#️⃣ macOS (Homebrew):

  brew install nmap


#️⃣ Python wrapper python-nmap:

  pip install python-nmap

Script: network-scanner.py

This README assumes your script is named network-scanner.py and contains the beginner-friendly host discovery code.

How to run

Open a terminal (Command Prompt / PowerShell on Windows, Terminal on macOS/Linux).

Navigate to the folder containing network-scanner.py.

Run the script:

  python network-scanner.py


The script runs host discovery on the default target 192.168.0.0/24.
To scan a different subnet, edit the simple_host_discovery("192.168.0.0/24") line near the bottom of the script.

Output

  The script creates a file named live_hosts.json in the same directory.

Example live_hosts.json structure:

  {
      "target": "192.168.1.0/24",
      "timestamp": "2025-10-30T12:34:56Z",
      "hosts_found": [
          {
              "ip": "192.168.1.5",
              "hostname": "device.local",
              "state": "up"
          },
          {
              "ip": "192.168.1.12",
              "hostname": "",
              "state": "up"
          }
      ]
  }

Troubleshooting

If you see “nmap executable not found”, install Nmap and ensure it’s on your PATH. Then re-open your terminal and run:

  nmap -v


to verify.

If python-nmap is missing:

  pip install python-nmap


If the script finds no hosts:
#️⃣ Verify your machine is on the same subnet you’re scanning.

#️⃣ Try a smaller target (e.g., a single IP like 192.168.1.1 or /30 range).

#️⃣ On some networks, ping may be blocked — consider using a TCP probe scan instead.

Security and Legal Notes

1️⃣ Only scan networks and devices you own or have explicit permission to scan.

2️⃣ Unauthorized scanning may be illegal or violate terms of service.