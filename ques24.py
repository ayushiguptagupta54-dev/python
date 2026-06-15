#  CHECK WHETHER TWO STRING ARE ANAGRAMS.
def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

s1 = "listen"
s2 = "silent"

if is_anagram(s1,s2):
    print("Anagram")
else:
    print("not anagram")
        
