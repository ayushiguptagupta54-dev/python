# COPY CONTENTS FROM ONE FILE TO ANOTHER
source = open("sample.txt", "r")
content = source.read()

destination = open("copu.txt", "w")
destination.write(content)

source.close()
destination.close()
print("File copied sucessfully")
