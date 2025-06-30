from port_scanner import scan_ports

print("💻 Penetration Testing Toolkit 💻")
print("1. Port Scanner")

choice = input("Select an option (1): ")

if choice == "1":
    target = input("Enter target IP or domain: ")
    ports = [21, 22, 23, 80, 443, 3306]
    scan_ports(target, ports)
