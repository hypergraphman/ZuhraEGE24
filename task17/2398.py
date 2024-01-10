f = open('17_2398.txt')
a = [int(x) for x in f]
b = []
for p1, p2, p3 in zip(a, a[1:], a[2:]):
    if (not (p1 > 0 and p1 % 10 == 9)) and (p2 > 0 and p2 % 10 == 9) and (not (p3 > 0 and p3 % 10 == 9)):
        b.append(p1 + p2 + p3)
print(len(b), max(b))