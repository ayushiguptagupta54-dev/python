def  find_name(names, target):
    left = 0
    right = len(names) -1
    while left <= right:
        mid = (left + right) // 2
        if names[mid] == target:
            return mid
        elif names[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

names = ["ayush", "shivam", "pooja", "riya" ]
target_name = "ayush"
result = find_name(names, target_name)
if result != -1:
    print("found at index", result)
else:
    print("Not found")


