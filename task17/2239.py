f = open('17_2239.txt')
a = [int(x) for x in f]
max_19 = max(filter(lambda x: x % 19 == 0, a))
print(max_19)
max_19 = float('-inf')
for x in a:
    if x % 19 == 0 and x > max_19:
        max_19 = x
print(max_19)
b = []
for p1, p2 in zip(a, a[1:]):
    if ((p1 > max_19) + (p2 > max_19)) >= 1:
        b.append(p1 + p2)
print(len(b), min(b))