# WRITE A FUNCTION  THAT ACCEPTS A LIST AND RETUN ONLY EVEN NUMBERS
def get_even_numbers(lst):
    even_numbers = []

    for num in lst:
        if num % 2 == 0:
            even_numbers.append(num)

    return even_numbers

# Example
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(get_even_numbers(numbers))
