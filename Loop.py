# count = 1
# while count <= 5:
#     print("Helloo")
#     count +=1
   
# i = 1
# while i <=5:
#     print("Ayush gupta", i)
#     i += 1

#  print numbers from 1 to 5
# i = 1
# while i <= 5:
#     print(i)
#     i += 1

#     print("Loop ended")

# i = 5
# while i >= 1:
#     print(i)
#     i -= 1

#     print("Loop ended")

# Practice questions 1 print the numbers from 1 to 100
# i = 1
# while i <= 100:
#     print(i)
#     i += 1

# Pratice questions 2 print the numbers from 100 to 1
# i = 100
# while i >= 1:       # Stopping condition
#     print(i)
#     i -= 1

# Pratice questions3 print the multiplication table of a number n
# n = int(input("Enter the number:"))
# i = 1
# while i <= 10:
#     print(19*i)
#     i += 1

# pratice questions 4 print the elements of the following list using a loop: (1,4,9,16,25,36,49,64,81,100)
# nums = (1,4,9,16,25,36,49,64,81,100)

# idx = 0
# while idx < len(nums):
#     print(nums[idx])  #nums[0], nums[1], nums[2]....
#     idx  += 1

# Pratice questions 5 Search for a number X in this tuple using loop: (1,4,9,16,25,36,49,64,81,100)
# nums = (1,4,9,16,25,36,49,64,81,100)

# x = 36

# i = 0
# while i < len(nums):
#     if(nums[i] == x):
#         print("Found at idx", i)
#         break
#     else:
#             print("Finding..")
#             i += 1

# print("End of the loop")

#  keyword Break  in loops
# i = 1
# while i <= 10:
#     print(i)
#     if(i == 5):
#         break     # stop the loop
#     i += 1
# print("Loop ended")

# i = 1
# while i <= 10:
#     if(i%2 == 0):
#         i += 1
#         continue   # skip the even numbers means skip the iteration
#     print(i)
#     i += 1

# i = 1
# while i <= 10:
#     if(i%2 != 0):
#         i += 1
#         continue   # skip the odd  numbers means skip the iteration
#     print(i)
#     i += 1

# Loops in python
# str = "AyushGupta"

# for char in str:
#     if(char == 'G'):
#         print("G found")
#         break
#     print(char)
# else:
#     print("Loop ended")

# Pratice questions 6 print the elements of the following list using a loop: [1,4,9,16,25,36,49,64,81,100]
# nums = [1,4,9,16,25,36,49,64,81,100]
# for el in nums:
#     print(el)

# Pratice questions 7 search for a number x in this tuple using loop: [1,4,9,16,25,36,49,64,81,100]
# nums = [1,4,9,25,36,49,64,81,100,49]
# x = 49

# idx = 6
# for el in nums:
#        if(el == x):
#         print("number found at idx", idx)

# idx += 1

seq = range(10)       # range stop
# print(seq[0])
# print(seq[1])
# print(seq[2])
# print(seq[3])

# for el in seq:
#     print(el)

# for el in range(2,10,2):   # range start, stop step
#     print(el)
# for i in range(2,101,2):
#     print(i)
# for i in range(1,101,2):
#     print(i)

# Pratice questions 8 print numbers from 1 to 100
# for i in range(101):
#     print(i)

# Pratice questions 9 print numbers from 100 to 1
# for i in range(100, 0, -1):
    #    print(i)

# Pratice questions 10 print the multiplications table of a number n
# n = int(input("Enter the number:"))
# for i in range(1, 11):
#     print(n*i)

    # Pass statement
# for i in range(5):
#         pass

# if i > 5:
#         pass 

#     print("some useful work")

# Pratice questions 11  WAP to print the sum of the first natural numbers.(using while)
# n = 3
# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i += 1
#     print("total sum =", sum)

# pratice questions 12 WAP to find the factorial of first n numbers.(using for)
n = 5
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
    print("factorial =", fact)
