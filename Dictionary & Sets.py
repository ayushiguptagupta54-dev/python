# Dictionary
info = {
    "name" :  "apna college",
    "subjects" : ["Python","c","java"],
    "topics" : ("dict", "sets"),
}
null_dict = {}
null_dict["name"] = "apnaschl"
print(null_dict)

print(info)
print(type(info))

info["name"]  = 'aayu'
info["surname"] = "gupta"
print(info)

info["name"]  = 34    # overwrite
info["surname"] = "gupta"
print(info)

student = {
    "name": "Aayu",
    "subjects": {
        "chem": 98,
        "phy": 67,
        "math": 45,
    }
}

# nested dictionary
# print(student)
print(student["subjects"]["chem"])
print(student["subjects"]["math"])
print((student.keys()))         # returns all keys
print(list(student.keys()))  
print(len(student))       
print((len(student.keys())))  
print(list(student.values()))       # retuns all value
print(student.items())         # returns all(key, val) pairs as tuples
print(student["name"])
print(student.get("name"))    # returns the key according to value
print("hi")
print("welcome to")
print("apna college")
print("we are learning")
print("coding")
student.update({"city" : "delhi"})      # inserts the specified items to the dictionary
print(student)
new_dict = {"city" : "delhi"}
student.update((new_dict))
print(student)
new_dict = {"name" : "neha kumari", "age" : 14}
student.update((new_dict))
print(student)

# Sets in python
collection = {1,3,4,5,6,3,6,1,"hellloo", "world"}
print(collection)
print(type(collection))
print(len(collection))    # total number of items
collection = {}           # empty dictionary
print(type(collection))
collection = {}           # empty dictionary
print(type(collection))
collection = set()         # empty set; syntax
collection.add(1)           # adds an element
collection.add(2)
collection.add(2)
collection.add(3)
collection.add("apna college")
collection.add((1,2,3))
print(type(collection))
print(collection)
collection.clear()         #empties the set
print(len(collection))

collection = {"hello", "apnaschl", "world", "coding", "python"}
print(collection.pop())      # removes a random value

set1 = {1,2,3}
set2 = {2,5,6}
print(set1.union(set2))      # combines both set values & returns new
set1 = {1,2,3}
set2 = {2,4,6}
print(set1.intersection(set2))      # combines common values & returns new

 # Pratice question 1  store following word meanings in a python dictionary : 
 # table : "a piece of furniture ", "list of facts & figures"
 # cat : "a small animals"

dictionary = {
  "cat" : "a small animal",
  "table": ["a piece of furniture", "listof facts & figures"]
 }
print(dictionary)
subjects = {
    "python", "java", "C++", "python", "Javascript", "java",
    "python", "java", "C++", "C"
}
print(subjects)

# Pratice questions 2 WAP to enter marks of 3 subjects from the user and store  them in a dictionary. start with an empty dictionary & add one by one. Use subjects name as key & marks as value
# marks = {}

# x = int(input("enter phy : "))
# marks.update({"phy" : x})
# x = int(input("enter math : "))
# marks.update({"math" : x})
# x = int(input("enter chem : "))
# marks.update({"chem" : x})
# print(marks)

# Pratice question 3 Figure out a way to store 9 & 9.0 as separate values in the set.(you can take help of built-in data types)
values = {9, 9.0,8,8.0,65}
print(values)
values = {"9", 9.0}
print(values)
values = {
    ("float",9.0),
    ("int", 9),
}
print(values)

print("Now we are start the python in loops")