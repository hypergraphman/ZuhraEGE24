mx = 0
mx_n = 0
for n in range(10, 131 + 1):
    line = '7' * n + '55'
    while '777' in line or '555' in line:
        if '777' in line:
            line = line.replace('777', '5', 1)
        else:
            line = line.replace('555', '7', 1)
    # print(n, line, line.count('5'))
    if line.count('5') >= mx:
        mx = line.count('5')
        mx_n = n
print(mx_n)