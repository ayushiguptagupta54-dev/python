#  function defination
# def calc_sum(a, b):   # function parameters
#     sum = a + b
#     print(sum)


# sum = calc_sum(5,10)    # function call: arguments

# # more lines of code

# calc_sum(3,7)

# # more lines of code
# calc_sum(6,9)

# def print_hello():
#   print("hello")

# output = print_hello()
# print(output)    # None

# # average of 3 numbers

# def calc_avg(a, b, c):
#     sum  = a + b + c
#     avg = sum / 3
#     return avg

# result = calc_avg(45, 67, 89)
# print(result)

# print("ayush", "aayu", end=" ")
# print("Hello world")

# def  cal_prod(a, b):
#     print(a + b)
#     return a * b

# result = cal_prod(4, 5)
# print(result)

# # Pratice question 1 WAF to print the length of a list.(list is the parameter)
# def print_list_length(lst):
#     print(len(lst))

# print_list_length([1, 2, 3, 4, 5])
# print_list_length(["car", "bus", "van", "bike", "cycle", "truck", "train", "aeroplane", "ship"])

# # Pratice question 2 WAF to print the elements of a list in a single ilne.(list in the prarpmeter)
# def print_len(list):
#     print(len(list))

#     def print_list(list):
#         for item in list:
#             print(item, end=" ")

#             print_list([1, 2, 3, 4, 5])
#             print()

# # Pratice question 3 WAF to find the factorial of n.(n is the parameter)
# n = 4
# fact = 1
# for i in range(1, n+1):
#     fact *= i
#     print(fact)

# # Pratice question 4 WAF to convert USD to INR

# def converter(usd_val):
#     inr_val = usd_val * 83
#     print(usd_val, "USD =", inr_val, "INR")
    
# converter(15)

# # homework questions
# fact = number=int(input("Enter the number:"))
# if(fact % 2 == 0):
#     print("even")
# else:
#     print("odd")


# Now we are learning recursions
#Recursive function to print n to 1
# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)
#     print("END")
# show(5)

# def fact(n):
#     if(n == 1 or n == 0):
#         return 1
#     return n * fact(n-1)

# print(fact(4))

# Pratice qestion 1 write a recursive function to calculate the sum of first n natural numbers
def calc_sum(n):
    if n == 1:
        return 1
        return n + calc_sum(n-1)
        print(calc_sum(5))

        # pratice questions 2 write a recursive function to print all elements in a list
        def print_list(list, idx=0):
            if (idx == len(list)):
                return
            print(list[idx])
            print_list(list, idx+1)
                                                                      
        fruit = ["apple", "banana", "mango"]
        print_list(fruit)