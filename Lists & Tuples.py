# marks = [98.3,78.2,55.4,89.7,99.45,22.2]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[3])
# print(len(marks)) 

# Lists in python
# student =["ayush",95.4,21, "goa"]
# print(student[3])
# student[0] = "aayu"
# print(student)

marks = [45,87,99,67,57]
print(marks[1:4])
print(marks[:4])
print(marks[1:])
print(marks[-3:-1])

list = [1,2,3,4]
list.append(5)   # adds one element at the end
print(list)
list = [1,2,3,4]
print(list.sort())  # sorts in ascending order

list = [1,5,7,8,3]
print(list.append(4))
print(list.sort(reverse=True))   # sorts in decending order
print(list)

list = ['a','c','g','d','i','j']
print(list.sort())
print(list)

list = ['a','c','g','d','i','j']
list.reverse()          # reverse list
print(list)

list = [1,4,6,7]
list.insert(1,5) # insert element at index
print(list)
                                             
list = [3,5,8,9,1,3]
list.remove(8)                           # remove the occurence of element
print(list)

list = [3,5,8,9,1]
list.pop(3)                           # remove the element at index
print(list)

# Tuple in python
tup = (1,4,3,6,7,2)
print(type(tup))
print(tup[0])
print(tup[1])

tup = ()
print(tup)
print(type(tup))

tup = (1,)
print(tup)
print(type(tup))

tup = (1,4,6,7,8,)
print(tup)
print(type(tup))

tup = (1,5,8,2,1,3)
print(tup[1:4])
print(type(tup))

tup = (4,6,1,4)
print(tup.index(1))          # returns index of first occurence

tup = (4,6,1,4)
print(tup.count(4))          # counts total occurence

# pratice questions   WAP to ask the user  to enter names of their 3 favorite movies and store them in a list.

# list = ("war2", "Baaghi2","Raaz")
# print(list)

# movies = []
# movies.append(input("enter 1st movie:"))
# movies.append(input("enter 2st movie:"))
# movies.append(input("enter 3st movie:"))

# print(movies)

# Pratice question 2 WAP to check if a list contains a palindrome of elements.(Hint:use copy()method)

list1 = ["m","a","a","m"]
list2 = [1,2,3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("it's not palindrome")

# pratice question 3 WAP to count the number of students with the "A" grade in the following tuple
grade = ("C","D","A","A","B","B","A")
print(grade.count("A"))   

# pratice question 4 store the above values in a lsit & sort them "A" to "D"
grade = ["C","D","A","A","B","B","A"]
grade.sort()
print(grade)



