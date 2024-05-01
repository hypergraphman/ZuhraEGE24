def f(s, c, m, ban):
    if c > m:
        return False

    if s >= 141:
        return c % 2 == m % 2
    moves = []
    if ban[0] == 0:
        moves.append(f(s + 2, c + 1, m, [1, 0, 0]))
    if ban[1] == 0:
        moves.append(f(s + 5, c + 1, m, [0, 1, 0]))
    if ban[2] == 0:
        moves.append(f(s * 3, c + 1, m, [0, 0, 1]))
    if (c + 1) % 2 == m % 2:
        return any(moves)
    else:
        return all(moves)


for s in range(1, 140):
    for m in range(1, 4 + 1):
        if f(s, 0, m, [0, 0, 0]):
            if m == 4:
                print(s)
            break