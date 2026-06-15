def has_dublicates_slow(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j and numbers[i] == numbers[j]:
                return True
    return False

numbers = [10, 30, 59, 10, 34]

result = has_dublicates_slow(numbers)
if result:
    print("dublicates found(slow)")
else:
    print("No duplicates found(slow)")