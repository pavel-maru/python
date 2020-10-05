
from itertools import count, cycle

for el in count(7):
    if el > 10:
        break
    else:
        print(el)

letters = ['a', 'b', 'c', 'd', 'e', 'f']

c = 0
for el in cycle(letters):
    if c > 10:
        break
    print(el)
    c += 1
