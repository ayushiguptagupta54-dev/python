# REMOVE DUBLICATES FROM A LIST.
def remove_dublicates(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list

list = [1,3,4,2,5,6,87,1,3,77,8,4,2,3,5]
print(remove_dublicates(list))


 