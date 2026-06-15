# SOME PRATICE QUESTION OF LIST FROM 11 to 15
# PRINT ALL PRIME NUMBERS BETWEEN 1 TO 100
# for num in range(1, 101):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#             else:
#                 print(num)

prime_numbers = []

for num in range(2, 101):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        prime_numbers.append(num)

print("Prime numbers between 1 and 100:")
print(prime_numbers)








