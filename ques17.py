# LIST PRATICE QUESTIONS FROM 17 TO 22..
# WRITE A PROGRAM TO FIND THE LARGEST ELEMENT IN A LIST.
numbers = [10, 25, 500, 40, 15]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest element:", largest)


