# PENETRATION-TESTING-TOOLKIT

A Python tool that checks which ports are open on a website or computer.

*COMPANY* : CODTECH IT SOLUTIONS

*NAME* : APOORVA S

*INTERN ID* : CT12DG815

*DOMAIN* : CYBER SECURITY AND ETHICAL HACKING 

*DURATION* : 12 WEEKS

*MENTOR* : NEELA SANTOSH KUMAR 

## Penetration Testing Toolkit - Python Project

Project Overview:

This project is a basic Penetration Testing Toolkit developed using Python. The main aim of the project is to create a beginner-friendly tool that helps identify basic security weaknesses in a network or computer system. According to the given task, the toolkit is modular, meaning it can be built with multiple tools like a port scanner, brute-forcer, or web vulnerability scanner. In this version, we’ve developed one working module: a Port Scanner.

What is a Port Scanner?

A Port Scanner is a tool used by cybersecurity professionals and ethical hackers to scan a computer or website and find out which ports (entry points) are open or closed. Ports are like digital doors used by various services (like websites, FTP, or emails). Knowing which ports are open helps security teams understand what services are running and if there are any possible vulnerabilities.

Some common ports:

Port 21: FTP (File Transfer)

Port 22: SSH (Remote login)

Port 80: HTTP (Web)

Port 443: HTTPS (Secure Web)

Port 3306: MySQL (Database)

About the Project:

The project uses Python’s socket library to perform port scanning. The code is kept simple and modular so that even beginners can understand and expand it. The scanner module is written in a separate file (port_scanner.py), and the main menu interface is in main.py. This clean structure allows easy additions later, like more scanning tools.

Files in the Project:

main.py – This is the starting point of the toolkit. It displays the menu and lets the user select the port scanner module.

port_scanner.py – This file contains the logic to scan multiple common ports and check whether they are open or closed.

README.txt – This file explains what the project does, how to use it, and details about each file.

How It Works:

Run main.py in Thonny.

The program displays:

" Penetration Testing Toolkit "

Choose option 1 for the Port Scanner.

Enter a target IP address or domain (like scanme.nmap.org).

The tool scans ports and tells which are open and which are closed.

Sample output:

swift
Copy
Edit
Scanning scanme.nmap.org...

[-] Port 21 is CLOSED  
[+] Port 80 is OPEN  
[-] Port 443 is CLOSED

Real-Time Usage:

This toolkit may be simple, but it has real-world applications in cybersecurity and IT:

Network Security Testing:

System admins can scan their own servers to check if any unnecessary ports are open, which could be entry points for hackers.

Ethical Hacking & Training:

Cybersecurity students use such tools to learn about vulnerabilities and practice scanning systems safely in labs.

Vulnerability Assessment:

Open ports may reveal outdated or unprotected services (like an old version of MySQL on port 3306), helping security teams fix them before attackers find them.

Firewall Testing:

After setting up a firewall, admins can use the tool to confirm that dangerous ports are properly blocked.

Important Note:

This tool is meant for educational use only and should never be used on websites or systems without permission.

Project Outcome:

This project successfully matches the given instructions:

It’s modular (uses multiple files)

Written in Python

Includes working functionality (port scanner)

Has clear documentation (README.txt)

Easy to test and extend

Later, more modules like brute-forcers, web vulnerability scanners, or file integrity checkers can be added to build a complete penetration testing suite.

Conclusion:

This Penetration Testing Toolkit project helped in understanding the basics of ethical hacking and cybersecurity using Python. By developing a simple yet functional Port Scanner, I learned how to identify open and closed ports on a system, which is an important part of vulnerability assessment.

The modular structure of the project makes it easy to expand by adding more tools like a brute-force module or web vulnerability scanner in the future. It also improved my Python skills, especially in working with network sockets and writing clean, organized code.
