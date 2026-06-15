# function pratice question from 27 tp 30
# CREATE A FUNCTION TO CHECK PRIME NUMBER
def is_prime(n):
    if n <= 1:
        return False

        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

num = 17
if is_prime(num):
    print("Prime number")
else:
                    print("not a prime number")
