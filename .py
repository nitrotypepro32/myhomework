# Program to check if a number is an Armstrong number

def is_armstrong_number(num):
    # Convert the number to a string to iterate over digits
    digits = str(num)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)
    return total == num

# Input from the user
number = int(input("Enter a number to check if it is an Armstrong number: "))

if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")