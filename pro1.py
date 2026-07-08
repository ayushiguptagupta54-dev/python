# #  1. import the random module
# import random

# #  2. create subjects
# subjects = [
#     "Ayushi gupta",
#     "Riya singh",
#     "Shivam gupta",
#     "pooja kumari",
#     "santosh"
# ]

# actions = [
#     "launched",
#     "cancled",
#     "ludo",
#     "Playing cricket",
#     "watching horror movies",
#     "dumping",
#     "seeing to him",
#     "celebrate the b'day party"
# ]

# places_or_things = [
#    " at knp", 
#    "gorakhpur",
#    "lucknow",
#    "jhasi",
#    "siddhnath",
#    "goa"
# ]

# while True:
#     subject = random.choice(subjects)
#     action = random.choice(actions)
#     place_or_thing = random.choice(places_or_things)

#     headline = f" BREAKING NEWS: {subjects} {actions} {place_or_thing}"
#     print("\n" + headline)

#     user_input = input("\nDo you want another headling? (yes\no)"). strip().lower()
#     if user_input == "no":
#         break
# #  print goodbye mesaage

# print("\nThanks for using fake news headline generator")


import random

subjects = [
    "Python Developer",
    "Cat",
    "Student",
    "AI Robot",
    "Monkey",
    "Teacher",
    "Programmer"
]

actions = [
    "discovers",
    "accidentally creates",
    "eats",
    "steals",
    "launches",
    "wins",
    "destroys"
]

objects = [
    "a time machine",
    "100 pizzas",
    "a secret algorithm",
    "the internet",
    "a flying car",
    "a giant banana",
    "a robot army"
]

places = [
    "in Kanpur",
    "at a college",
    "inside a library",
    "on the Moon",
    "at a coding interview",
    "during an online class"
]

print("\n📰 BREAKING NEWS 📰\n")

headline = (
    f"{random.choice(subjects)} "
    f"{random.choice(actions)} "
    f"{random.choice(objects)} "
    f"{random.choice(places)}!"
)

print(headline)
