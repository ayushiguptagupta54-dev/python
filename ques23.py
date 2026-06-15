# string pratice question from 23 to 26
# WRITE A PROGRAM TO COUNT THE FREQUENCY OF EACH CHARACTER IN A STRING

def char_frequency(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

# Example usage
text = "ayushivam"
result = char_frequency(text)
print(result)

