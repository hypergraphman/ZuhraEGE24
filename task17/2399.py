a = [int(x) for x in open('17_2399.txt')]
# s = sum(sum(map(int, str(x)) for x in a))
# print(s)
s = 0
for x in a:
    if x % 35 == 0:
        while x:
            s += x % 10
            x //= 10
print(s)
b = []
for p1, p2 in zip(a, a[1:]):
    if (p1 > s and p2 <= s and hex(p2)[-2:] == 'ef') or (p2 > s and p1 <= s and hex(p1)[-2:] == 'ef'):
        b.append(p1 + p2)
print(len(b), min(b))