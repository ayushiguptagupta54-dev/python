list = [2,345,6,63,68,99]
print(list)
print(type(list))
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])
print(list[5])

lst1 = [1, 2, 2, 3, 5, 4, 6]
lst2 = ["Red", "Green", "Blue"]
print(lst1)
print(lst2)

details = ["Abhijeet", 18, "FYBScIT", 9.8]
print(details)

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]
print(colors[2])
print(colors[4])
print(colors[0])

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [-5]    [-4]    [-3]     [-2]      [-1]
print(colors[-1])
print(colors[-3])
print(colors[-5])

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
if "Yellow" in colors:
    print("Yellow is present.")
else:
    print("Yellow is absent.")

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
if "Orange" in colors:
    print("Orange is present.")
else:
    print("Orange is absent.")

print(list[:4])



list = [i for i in range(10)]
print(list)
list = [i*i for i in range(21) if i%2==0]
print(list)

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)

