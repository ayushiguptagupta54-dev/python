#  FIND THE SECOND LARGEST NUMBER IN A LIST.
def second_largest(list):
    largest = list[0]
    second = list[0]
    for num in list:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    return second

list = [23,4,7,889,32,56,87,90]
print(second_largest(list))











