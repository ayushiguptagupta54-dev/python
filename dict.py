# """
# "ravi@gamil.com -> ravi sharma
# "priya@gamil.com  -> priya
# """
users = {}

#  Insert
users["ravi@gmail.com"] = "ravi sharma"
users["priya@gmail.com"] = "priya patel"
users["chirag@gamil.com"] = "chairag singh"

print(users["ravi@gmail.com"])

print("priya@gmail.com in users")


users["priya@gmail.com"] = "priya sharma"
print(users)

del users["chirag@gamil.com"]
print(users)
print(users.keys())
print(users.values())




