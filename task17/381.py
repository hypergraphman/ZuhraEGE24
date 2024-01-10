a = [int(el) for el in open('17-381.txt')]
mx39 = max(filter(lambda el: 1000 <= abs(el) < 10000 and abs(el) % 100 == 39, a))
print(mx39)
mx39 = float('-inf')
for el in a:
    # if len(str(abs(el))) == 4 and str(el)[-2:] == '39'
    if 1000 <= abs(el) < 10000 and abs(el) % 100 == 39 and el > mx39:
        mx39 = el
print(mx39)
res = []
for p1, p2 in zip(a, a[1:]):
    if (1000 <= abs(p1) < 10000) + (1000 <= abs(p2) < 10000) == 1 and (p1 + p2) ** 2 <= mx39 ** 2:
        res.append(p1 + p2)

print(len(res), max(res))

