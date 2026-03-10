#  Dictionaries in python
dic = {
    "Ayush": "Human being",
    "spoon": "object"
}
print(dic["Ayush"])
print(dic["spoon"])
dic = {
313: "shubham",
221: "ayush",
111: "shivam",
}
print(dic[111]) 

# info  = {'name': 'kaju', 'age': 2}
# print(info['name'])
# print(info['age'])


info  = {'name': 'kaju', 'age': 2}
print(info)
print(info.keys())
print(info.values())

for key in info.keys():
    print(f"{key}: {info[key]}")

    info  = {'name': 'kaju', 'age': 2}
print(info.items())
for key , values in info.items():
    print(f"The value corresponding to the key {key} is {values}")