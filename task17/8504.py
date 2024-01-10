f = open('17_8504.txt')
a = [int(x) for x in f]
mn = float('inf')
for el in a:
    if 100 <= abs(el) <= 999 and abs(el) % 10 == 5:
        mn = min(el, mn)

b = []
for p1, p2 in zip(a, a[1:]):
    if (100 <= abs(p1) <= 999 or 100 <= abs(p2) <= 999) and (p1 + p2) % mn == 0:
        b.append(p1 + p2)
print(len(b), max(b))
