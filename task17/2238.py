f = open('17_2238.txt')
a = [int(x) for x in f]
avg = sum(a) / len(a)
b = []
for p1, p2, p3 in zip(a, a[1:], a[2:]):
    if ((p1 > avg) + (p2 > avg) + (p3 > avg)) >= 2:
        b.append(p1 + p2 + p3)
print(len(b), max(b))