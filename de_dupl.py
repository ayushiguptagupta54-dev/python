signups = [
    "ravi@gmail.com",
    "shiva@gmail.com",
    "shiv@gmail.com",
    "shivam@gmail.com",
    "ayush@gmail.com",
    "ravi@gmail.com",
    "om@gmail.com",
    "ravi@gmail.com"
]

def remove_dup(emails):
    seen = set()
    unique = []

    for email in emails:
        if email not in seen:
            unique.append(email)
            seen.add(email)
        return unique

clean = remove_dup(signups)          
print(clean)

