from re import fullmatch

k = 0
for i in range(131, 10 ** 8, 131):
    if fullmatch(r'[0123456789]*13\d\d*\d1\d*', str(i)):
        k += 1
        if k % 1131 == 0:
            print(i, i // 131)
