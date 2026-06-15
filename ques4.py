# WRITE A PROGRAM TO CHECK WHETHER A NUMBER A YEAR IS YEAR IS A LEAP YEAR OR NOT
year = int(input("Enter a year:"))
if (year % 4 == 0 and year % 100 != 0  or year % 400 == 0):
    print("The year is leap year")
else:
        print("The year is not a leap year")




        
