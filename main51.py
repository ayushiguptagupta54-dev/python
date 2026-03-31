#  Seek() in python
# with open('file.txt', 'w') as f:
#     print(type(f))
#     #  Move to the 10th byte in the file.
#     f.seek(10)
#     #  reas the next 5 bytes
# print(f. tell())
# data = f.read(5)
# print(data)


# Truncate in python
with open('sample.txt', 'w') as f:
    f.write('hello world')
    f.truncate(2)

    with open('sample.txt','r') as f:
        print(f.read())

