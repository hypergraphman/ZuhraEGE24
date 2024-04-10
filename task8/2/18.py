from itertools import permutations

words = [''.join(word) for word in permutations('перевыборы', r=10)]
a = set()
for word in words:
    t = word.replace('п', '1').replace('е', '0').replace('р', '1').replace('в', '1').replace('ы', '0').replace('б', '1').replace('о', '0')
    if '00' not in t and '11' not in t:
        a.add(word)
print(len(a))