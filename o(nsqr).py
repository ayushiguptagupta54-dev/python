def find_dublicates(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j and numbers[i] == numbers[j]:
                return True
    return False
numbers = [12,54,76,48,48,26,85]

result = find_dublicates(numbers)
if result:
    print("dublicates found")
else:
    print("No dublicates found")


