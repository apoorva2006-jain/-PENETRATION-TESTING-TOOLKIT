import socket

def scan_ports(target, ports):
    print(f"\nScanning {target}...\n")
    for port in ports:
        try:
            s = socket.socket()
            s.settimeout(1)
            s.connect((target, port))
            print(f"[+] Port {port} is OPEN")
            s.close()
        except:
            print(f"[-] Port {port} is CLOSED")
