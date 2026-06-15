# FIND THE LONGEST WORD IN A SENTENCE
sentence = "Python is a powerful programming language"

words = sentence.split()

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)

