mx = 0
mn_n = 500
for n in range(500, 1000 + 1):
    s = '3' * n
    while '111' in s or '3333' in s:
        if '111' in s:
            s = s.replace('111', '33', 1)
        else:
            s = s.replace('333', '1', 1)
    if int(s) > mx:
        mx = int(s)
        mn_n = n
print(mx, mn_n)
