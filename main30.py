#   Recursion in python
def factorial(n):
    if (n ==0 or n ==1):
        return 1
        
    else:
        return n*factorial(n-1)

print(factorial(3))
print(factorial(5)) 

#  Write a program of fibonachi series using recursion.
def fibonachi(n):
    if(n== 0 or n==1):
        return n
    else:
        return fibonachi(n-1) + fibonachi(n-2)

print(fibonachi(3))
        #  0 1 1 2 3 5 8 13 21.....
