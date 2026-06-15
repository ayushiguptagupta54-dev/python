# READ A FILE AND COUNT NUMBER OF WORDS
file = open("Sample.txt", "r")
content  = file.read()
words = content.split()
print("Numbers of words:", len(words))
file.close()


