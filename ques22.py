# REVERSE THE LIST WITHOUT USING REVERSE()
lst = [10, 20, 30, 40, 50]

reversed_list = []

for i in range(len(lst) - 1, -1, -1):
    reversed_list.append(lst[i])

print("Reversed List:", reversed_list)

