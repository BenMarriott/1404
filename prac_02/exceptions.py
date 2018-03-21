"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? When usings floating point numbers
2. When will a ZeroDivisionError occur? When attempting n/0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""
"""""
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
    """""
"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    try:
        result = int(input("Please enter an integar: \n"))   # TODO: this line
        finished = True
    except (ValueError):  # TODO - add something after except
        print("Please enter a valid integer.\n")
print("Valid result is:", result)