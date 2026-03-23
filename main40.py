# Exercise number 4:
# Write a python program to translate amessage into secrret code language. Use the rules below to translate normal english into secret code langugae.
# coding:
# If the word contains atleast 3 characters, remove the first letter and append it at the end 
# now append three random characters at the starting  and the end
# else:
# simply reverse the string
# 
# Decoding:
# if the word conatins less than 3 characters , reverse it 
# else:
# remove 3 random characters from start and end. Now remove the last letter and append it to the begining
# 
# Your program should ask whether you want to code or decode.
import random
import string
def encode_message(message):
    words = message .split()
    encoded_words = []
    for word in words:
        if len(word) >= 3:
            # Remove the first letter and append it at the end
            word = word[1:] + word[0]
            # Append three random characters at the start and end
            random_chars = ''.join(random.choices(string.ascii_letters, k=3))
            word = random_chars + word + random_chars
        else:
            # Simply reverse the string
            word = word[::-1]
        encoded_words.append(word)
    return ' '.join(encoded_words)
    def decode_message(encoded_message):
        words = encoded_message.split()
        decoded_words = []
        for word in words:
            if len(word) >= 9:   
                #  remove 3 random characters from start and end
                word = word[3: -3]
                #  remove the last letter and append it to the beginning
                word = word[-1] + word[:-1]
            else:
                #  reverse the string
                word = word[::-1]
        decoded_words.append(word)
    return ' '.join(decoded_words)
    