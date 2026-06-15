# def merge_sort(numbers):

#       if len(numbers) <= 1:
#         return arr

#         middle = len(arr) // 2

#         left_half = numbers[middle]
#         right_half = numbers[middle]

#         print(f"splitting: {numbers}")
#         print(f"left: {left_half}")
#         print(f"right: {right_half}")

#         sorted_left = merge_sort(left_half)
#         sorted_right = merge-sort(right_half)

#         sorted_result = combine(sorted_left, sorted_right)

#         print(f"merged back: {sorted_result}")

#         return sorted_result

# def combine(left, right): 

#     final_list = []
#     left_pointer = 0
#     right_pointer = 0

#     while left_pointer < len(lft) and right_pointer < len(right):

#         left_item = left[left_pointer]
#         right_item = right[right_pointer]

#         if left_item <= right_item:
#             final_list.append(left_item)
#             left_pointer = left_pointer + 1
#         else:
#             final_list.append(right_item)
#             right_pointer = right_pointer + 1
               
#     remaining_left = left[left_pointer:]
#     remaining_right = right[right_ponter:]

#     final_list = final_list + remaining_left + remaining_right

#     return final_list

# prices = [850, 200, 520, 100, 430]
# result = merge_sort(prices)
# print("final result", result)



def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


arr = [38, 27, 43, 356758, 9255, 8258587, 10]
sorted_arr = merge_sort(arr)

print("Original Array:", arr)
print("Sorted Array:", sorted_arr)

