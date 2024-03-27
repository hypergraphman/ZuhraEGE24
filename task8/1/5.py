from itertools import product

words = [''.join(word) for word in product('диляра', repeat=6)]
k = 0
for word in words:
    if word.count('д') == 1 and word.count('р') == 1 and word.count('и') <= 1:
        k += 1
print(k)