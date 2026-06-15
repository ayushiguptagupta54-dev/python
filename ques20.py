# sort the list without using the sort ()
# numbers = [64, 34, 25, 12, 22, 11, 90]

# n = len(numbers)

# for i in range(n):
#     for j in range(0, n - i - 1):
#         if numbers[j] > numbers[j + 1]:
#             # Swap elements
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# print("Sorted List:", numbers)

numbers = [45,76,21,6,3,8,76,89,43,68653,65,42,75,55,87,24,76,98053,6576,524,78]
n = len(numbers)
for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted List:", numbers)
