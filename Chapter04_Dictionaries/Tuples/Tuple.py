ips = {}
answer = "Y"
while answer == "Y":
    ips[(input("Enter the first two octets: "),
         input("Enter the two last octets: "))] = input("Machine name: ")
    answer = input("Type 'Y' to continue: ").upper()

# Displaying the IPs
print("Displaying IPs: ")
for ip in ips.keys():
    print(ip[0] + "." + ip[1])

    #Displaying machines with the same IP address
    print("Displaying machines with the same address: ")
    search = input("Enter the last two octets: ")
    for ip, name in ips.items():
        print("Machines in the same address (different networks): ")
        if(ip[1] == search):
            print(name)

            # Displaying machines from the same network
            print("Displaying machines from the same network: ")
            network = input("Enter the first two octets: ")
            for ip, name in ips.items():
                if(ip[0] == network):
                    print(name)

