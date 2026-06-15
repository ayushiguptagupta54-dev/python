# CREATE A STUDENT MANAGEMENT SYSTEM USING DICTIONARY

stu = {}

while(True):
    print("\n1. Add students")
    print("2. view students")
    print("3. search students")
    print("4. exit")

    choice = input("Enter a choice")

    if choice == "1":
        roll = input("Enter roll no:")
        name = input("Enter a name: ")
        students[roll] = name
        print("Student added sucessfully")

    elif choice == "2":   
        for roll, name in students.items():
            print(f"Roll no: {roll}, Name: {name}")

    elif choice  == "3":  
        roll = input("Enter roll noi:")
        if roll in students:
            print("STudent nmae:", students[roll])

        else:  
            print("Student not found")

    elif choice == "4":
        break
    else:
        print("Invalid choice")


