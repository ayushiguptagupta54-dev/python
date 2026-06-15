# FIND THE COMMON ELEMENT BETWEEN TWO LIST
def common_element(list1, list2):
    common = []
    for element in list1:
        if element in list2:
            common.append(element)
    return common

list1 = [1,2,5,4,62,57,7,8,9]
list2 = [33,54,67,87,32,1,2,5,6,9]
print(common_element(list1, list2))

