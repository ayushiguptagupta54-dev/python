# COVERT LOWERCASE LETTERS INTO UPPERCASE WITHOUT USING UPPER()
s = "hello world i am ayushivam forever togehter made for each other but density has not want to be together"
result = ""
for char in s:
    if'a' <= char <= 'z':
        result += chr(ord(char) -32)
    else:
            result += char

print(result)



