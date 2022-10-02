"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    A ValueError will occur when anything but an integer is input
2. When will a ZeroDivisionError occur?
    A ZeroDivisionError if you try and divide by zero
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    You could do an error checking loop to make sure the denominator is greater than 0
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator <= 0:
        print("The denominator should be greater then 0")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

