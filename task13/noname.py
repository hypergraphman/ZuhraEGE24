from ipaddress import ip_network

net = ip_network('192.168.248.176/255.255.255.240', False)
k = 0
for ad in net:
    # t = bin(int(ad))[2:].rjust(32, '0')
    t = f'{int(ad):0>32b}'
    if t.count('0') == t.count('1'):
        k += 1
print(k)
