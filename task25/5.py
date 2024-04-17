from re import fullmatch

for i in range(157, 10 ** 10, 157):
    if fullmatch(r'1[13579]*3456[24680]8', str(i)):
        print(i, i // 157)
