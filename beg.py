users = [
    "ram@gmail.com",
    "ayush@gmail.com",
    "shivam@gmail.com"
#  49.99M
]

def login(email):
    for user in users:
        if user == email:
            return "login succesfully"
    return "User not found"

print(login("ram@gmail.com"))



