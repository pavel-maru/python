# Ok
from functools import reduce

def my_f(a, b):
    return a * b

my_list = [el for el in range(100,1001) if el % 2 == 0]
print(my_list)

print(reduce(my_f, my_list))

# res = 1
# for el in new_list:
#     res = res * el
# print(res)
