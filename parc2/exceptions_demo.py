"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""


finished = False

while not finished:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator(none zeros): "))
        fraction = numerator / denominator
        print(fraction)
        finished = True
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
print("Finished.")

'''
1. when there is a character
2. when the denominator is 0
3. maybe
'''