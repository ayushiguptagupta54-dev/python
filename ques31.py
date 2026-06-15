# dictionary question from 31 to 34
# COUNT WORD FREQUESNCY IN A SENTENCES USING DICTIONARY
sentences = "python is easy and python is powerful"

words = sentences.split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1
print(freq)
