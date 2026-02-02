#  break
# for i in range(12):
#     if(i == 10):
#        break
#     print("5 X", i, "=", 5 * (i + 1))

# print("Loop end")
 
#  continue

for i in range(12):
    if(i == 10):
        print("Skip the loop")
        continue
    print("5 X", i, "=", 5 * (i + 1))

  
#  Do while loop

i = 0
while True:
    print(i)
    i = i + 1
    if(i%100 == 0):
        break
    # print("loop end")