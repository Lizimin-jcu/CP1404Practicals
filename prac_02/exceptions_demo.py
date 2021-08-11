"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""
print("Warning : The denominator can't be zero!!!")
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

#1. When will a ValueError occur?
#When the input number is decimal,it will make a ValueError.

#2. When will a ZeroDivisionError occur?
#When the denominator is 0,it will occur ZeroDivisionError.

#3.