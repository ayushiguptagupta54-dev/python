#  Map filter, reduce

#  Map
# def cube(x):
#      return x *x*x

# print(cube(3))

# l = [1,4,6,7,8,9,22]
# # newl = []
# # for item in l:
# #  newl.append(cube(item))

# newl = list(map(lambda x: x * x* x, l))

# # print(newl)

# #  Filter
# def filter_function(a):
#     return a>9

# newnewl = list(filter(filter_function, l))
# print(newnewl)

#  reduce
from functools import reduce

numbers = [1,2,3,4,5,6,8,]
def mysum(x, y):
    return x + y

sum = reduce(mysum, numbers)

print(sum)

