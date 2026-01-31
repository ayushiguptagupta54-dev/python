# Reading in a file

# f = open("demo.txt", "r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()


# f = open("demo.txt", "r")

# data = f.read(5)
# print(data)

# f.close()

# f = open("demo.txt", "r")

# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# f.close()


# writing in a file
# f = open("demo.txt", "a")
# f.write("\n now im doing python")
# f.close()

# #  f = open("demo.txt", "a")
# # f.write("Now i am doing coding in python")
# # f.close()


# f = open("sample.txt", "w")
# f.close()

# f = open("demo .txt","r+")
# # f.write("abc")
# print(f.read())
# f.write("abc")
# f.close()

# with open("demo.txt", "r") as f:
#     data = f.read()
#     print(data)


# with open("demo.txt", "w") as f:
#     f.write("new data")

# # deleting in a file
# import os
# os.remove("demo.txt")

 # pratice questions 1 create a file "pratice.txtt" using pytrhon. Add the following data in it:
with open("pratice.txt","w") as f:
    f.write("HI everyone\nwe are learning fileI\o\n")
    f.write("using java.\ni like programming in java.")


# pratice questions 2 WAF that replace all occurence of java with python in above file.


with open("pratice.txt","r") as f:
    data = f.read()

    new_data = data.replace("java", "python")
    print(new_data)

with open("pratice.txt","w") as f:
    f.write(new_data)


    #pratice question 3
word = "learning"
with open("pratice.txt","r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("found")
    else:
            print("not found")


# Pratice 4  waf to find in which line of the file does the word "learning" occur first.
def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("pratice.txt","r") as f:
        while data:
            data  = f.readline()
            if(word in data):
                print(line_no)
                return
                line_no += 1



print(check_for_line())


# Pratice question 5 from a file containning a umbers separated by comma, print the count of the even number

with open("pratice.txt","r") as f:
    data = f.read()
    print(data)

nums = data.split(",")
print(nums)