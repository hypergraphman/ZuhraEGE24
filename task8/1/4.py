from itertools import product

words = [''.join(word) for word in product(sorted('маоулицей')[::-1], repeat=6)]

for i, word in enumerate(words, start=1):
    if word == 'умелец':
        print(i, word)