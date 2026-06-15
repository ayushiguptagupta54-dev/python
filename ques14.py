#  WRITE A PROGRAM TO CHECK WHETHER A NUMBER IS ARMSTRONG OR NOT
num = int(input("Enter a number: "))
temp = num
digit = len(str(num))
sum = 0
while temp > 0:
    d = temp % 10
    sum += d ** digit
    temp //= 10
if num == sum:
    print("It's armstrong number")
else:
    print("It's not an armstrong number")

