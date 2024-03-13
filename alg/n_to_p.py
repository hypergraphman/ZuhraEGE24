from string import digits, ascii_uppercase


def n_to_p(n, p):
    r = ''
    # alp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alp = digits + ascii_uppercase
    while n:
        r = alp[n % p] + r
        n //= p
    return r


print(int('asdf', 36))
print(n_to_p(503331, 36))