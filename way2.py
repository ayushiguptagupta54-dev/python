def has_dublicates_fast(numbers):
    seen = set()
    for number in numbers:
        if number in seen:
            return True
            seen.add(number)

        return False

numbers = [10, 20, 443,65,87,10]
result = has_dublicates_fast(numbers)
if result:
    print("dublicates found(fast)")
else:
    print("No duplicates found(fast)")

