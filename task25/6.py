def divs(n):
    d = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return sorted(d)


def M(n):
    d = divs(n)
    if len(d) == 0:
        return 0
    return d[0] + d[-1]


n = 777828 + 1
k = 5
while k:
    if abs(M(n)) % 100 == 16:
        print(n, M(n))
        k -= 1
    n += 1
