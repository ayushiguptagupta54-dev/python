# WRITE A PROGRAM TO COUNT VOWELS AND CONSONANTS IN A STRING
def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    v_count = 0
    c_count = 0

    for ch in s:
        if ch.isalpha():  # check if character is a letter
            if ch in vowels:
                v_count += 1
            else:
                c_count += 1

    return v_count, c_count

# Input
text = input("Enter a string: ")
v, c = count_vowels_consonants(text)

print("Vowels:", v)
print("Consonants:", c)

