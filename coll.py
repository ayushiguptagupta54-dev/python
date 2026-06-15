
import hashlib

hashlib.sha256("ravi@gmail.com".encode()).hexdigest()




users = {}

#  insert
users["ravi@gmail.com"] = "Ravi sharma"
users["priya@gmail.com"] = "Priya patel"
users["ayush@gmail.com"] = "Ayush"

#  key = "ravi@gmail.com"
# value = "Ravi sharma"
#  box = hash(key) % total_boxes
# store(box, "Ravi sharma")

print(hash("ravi@gmail.com"))
print(hash("priya@gmail.com"))
print(hash("ayush@gmail.com"))

