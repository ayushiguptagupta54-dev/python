def clean(names):

    left = 0
    for right in range(1,len(names)):
        if names[right] != names[left]:
            left = left = 1
            names[left] = names[right]

    return left + 1

names = ["ayush", "ayushi","shivam", "shivam", "riya", "keshav"]
count = clean(names)
print(names[:count])

