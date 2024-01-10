f = open('17_2401.txt')
a = [int(x) for x in f]
b = []
for p1, p2 in zip(a, a[1:]):
    if 50 <= abs(p1) + abs(p2) <= 200:
        b.append(min(p1, p2))
print(len(b), min(b))