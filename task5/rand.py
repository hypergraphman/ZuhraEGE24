def f(n):
    s1 = bin(n)[2:]
    if s1.count('1') > s1.count('0'):
        s2 = s1 + '0'
    else:
        s2 = s1 + '1'
    if s2.count('1') > s2.count('0'):
        s3 = s2 + '0'
    else:
        s3 = s2 + '1'
    return int(s3, 2)


res = []
for i in range(2, 1000):
    if f(i) < 57:
        res.append(f(i))
print(max(res))