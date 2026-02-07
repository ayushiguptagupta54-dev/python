tuple1 = (0,3,51,6,7,1,4,3,2,3,3,4,3)
# res = tuple1.count(3)
# # res = tuple1.index(3)
# # res = tuple1.index(3,4,8)
res = len(tuple1)
print('length of tuple1 is:', res)

countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       # add item 
temp.pop(3)                 # remove item
temp[2] = "Finland"         # change item
countries = tuple(temp)
print(countries)














