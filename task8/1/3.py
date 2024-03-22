from itertools import product

words = [''.join(word) for word in product(sorted('аитовру'), repeat=5)]

for i, word in enumerate(words, start=1):
    if word == 'товар':
        print(i, word)