#  Tuples in python

tup = ( 1,43,657,8,4,2,5,)
print(type(tup), tup)
print(len(tup))
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])
print(tup[5])

if 657 in tup:
    print("Yes tup is present in tup")
    tup2 = tup[1:5]
    print(tup2)
else:
        print("tup is not present")


tuple1 = (1, 2, 2, 3, 5, 4, 6)
tuple2 = ("Red", "Green", "Blue")
print(tuple1)
print(tuple2)

details = ("Abhijeet", 18, "FYBScIT", 9.8)
print(details)


#  Tuples indexing
country = ("Spain", "Italy", "India", "England", "Germany")
#            [0]      [1]      [2]       [3]        [4]


#   tuples positive indexing
country = ("Spain", "Italy", "India", "England", "Germany")
#            [0]      [1]      [2]       [3]        [4]
print(country[1])
print(country[3])
print(country[0])


#  tuples negative indexing
country = ("Spain", "Italy", "India", "England", "Germany")
#            [0]      [1]      [2]       [3]        [4]
print(country[-1])
print(country[-3])
print(country[-4])
    
# check for item
country = ("Spain", "Italy", "India", "England", "Germany")
if "Germany" in country:
    print("Germany is present.")
else:
    print("Germany is absent.")

#  range of index
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[3:7])     # using positive indexes
print(animals[-7:-2])   # using negative indexes















