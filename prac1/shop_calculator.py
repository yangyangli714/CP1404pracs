"""
CP1404/CP5632 - Practical
Shop calculator
"""

total = 0
number = int(input("Number of items (Need to be in numbers): "))
while number < 0:
    print("Invalid number of items! NEED TO BE IN INTEGER")
    number = int(input("Number of items (Need to be in numbers): "))
for i in range(0, number):
    price = float(input("Price of item: $"))
    total += price
if total > 100:
    total *= 0.9
print("Total price for ", number, " items is $", total)

