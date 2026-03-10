#  Dictionary methods in python
ep1 = {221: 32, 212:44,576: 78}
print(ep1)
ep2 = {334: 5546, 7492: 2133, 9474: 4827}
print(ep2)
ep1.update(ep2)
print(ep1[334]) 

# 1.  create a new key and assign a value to it.
info = {'name': 'Karan', 'age': 19, 'eligible': True}
print(info)
info['DOB'] = 2001
print(info)

#  2. use the update method
info = {'name': 'Karan', 'age': 19, 'eligible': True}
print(info)
info.update({'age': 20})
info.update({'DOB': 2001})
print(info)

# 3. removing item from dictionary
info = {'name': 'Ka ran', 'age': 19, 'eligible': True}
info.clear()
print(info)

#  4. pop method
info = {'name': 'Karan', 'age': 19, 'eligible': True}
info.pop('eligible')
print(info)

info = {'name': 'Karan', 'age': 19, 'eligible': True, 'DOB': 2003}
info.popitem()
print(info)

#  5. copy method
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
newDictionary = info.copy()
print(newDictionary)
