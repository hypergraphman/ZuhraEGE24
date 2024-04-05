from itertools import permutations

words = [''.join(word) for word in permutations('ТИМУР', r=4)]
a = set()
for word in words:
    t = word.replace('Т', '1').replace('И', '0').replace('М', '1').replace('У', '0').replace('Р', '1')
    if '00' not in t and '11' not in t:
        a.add(word)
print(len(a))