#  Reading a file
f = open('myfile.txt', 'r')
print(f)
text = f.read()
print(text)
f.close()

#  Writing a file

f = open('myfile.txt', 'a')
f.write('Hey i am ayush')
f.close()

f = open('myfile.txt', 'r')
# ... do something with the file
f.close()
