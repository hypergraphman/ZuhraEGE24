from ipaddress import ip_network

net = ip_network('192.168.32.160/255.255.255.240', False)
k = 0
for address in net:
    if bin(int(address)).count('1') % 2 == 0:
        k += 1
print(k)