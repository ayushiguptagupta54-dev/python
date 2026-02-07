# solution of exercise 2

import time
t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))

hour = int(input("Enter hour: "))
print(hour)

if(hour>=0 and hour<12):
    print("GOOD MORNING AYUSH")
elif(hour>=12 and hour<17):
        print("GOOD AFTERNOON AYUSH")
elif(hoiur>=17 and hour<0):
 print("GOOD NIGHT AYUSH")


