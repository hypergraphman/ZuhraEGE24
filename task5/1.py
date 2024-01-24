def f(n):
    d1, d2, d3 = n // 100, n // 10 % 10, n % 10
    # d1, d2, d3 = map(int, str(n))
    s1 = d1 + d2
    s2 = d2 + d3
    a = sorted([s1, s2])[::-1]
    r1, r2 = map(str, a)
    return r1 + r2


# print(f(138))
for i in range(100, 1000):
    if f(i) == '145':
        print(i)
