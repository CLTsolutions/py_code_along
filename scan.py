# multi line string
menu = """\
*** PORT SCANNER MENU ***
1) add ip
2) add port
3) enumerate
4) exit
"""

ips = []
ports = []
while True:
    print(menu)
    choice = input("> ")
    print(choice)
    if choice == "1":
        new_ip = input("ip: ")
        ips.append(new_ip)
    elif choice == "2":
        new_port = input("ports: ")
        ports.append(new_port)
    elif choice == "3":
        for ip in ips:
            for port in ports:
                # like string interpolation in js
                print(f"{ip}:{port}")
    elif choice == "4":
        break;

print(ips, ports)