#  CREATE A FUNCTION TO CALCULATE THE LCM AND HCF
def calculate_lcm_hcf(num1, num2):
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            hcf = i
            lcm = (num1 * num2) // hcf
            return lcm, hcf

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

lcm, hcf = calculate_lcm_hcf(num1, num2)
print(f"LCM: {lcm}, HCF: {hcf}")
