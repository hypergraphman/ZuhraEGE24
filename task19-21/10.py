def f(s, c, m, b):
    if c > m:
        return False

    if s >= 141:
        return c % 2 == m % 2
    moves = [f(s + 1, c + 1, m, 0),
             f(s + 2, c + 1, m, 0)]
    if b == 0:
        moves.append(f(s * 3, c + 1, m, 1))
    if (c + 1) % 2 == m % 2:
        return any(moves)
    else:
        return all(moves)


for s in range(1, 140):
    for m in range(1, 4 + 1):
        if f(s, 0, m):
            if m == 4:
                print(s)
            break