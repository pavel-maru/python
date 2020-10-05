# Ok
#def fact(n):
#    res = 1
#    for num in range(1, n + 1):
#        res = res * num
#    return res

def fact(n):
    for el in range(1, n):
        yield el

n = 5
f = 1

for el in fact(n + 1):
    f = f * el

print(f)


#import sys
#sys.path.insert(0, 'path')
#for i in sys.path:
#    print(i)

