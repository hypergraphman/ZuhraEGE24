f = open('17_2004.txt')
a = []
for x in f:
    x = int(x)
    if x % 13 == 4 and x % 8 == 1:
        a.append(x)
print(max(a), sum(a))