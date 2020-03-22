"""
CP1404/CP5632 - Practical
Loops
"""
# Loop displays all of the odd numbers between 1 and 20
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# Count in 10s from 0 to 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# Count down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# Print n stars
number_of_stars = int(input("Number of stars: "))
for i in range(0, number_of_stars):
    print('*', end=' ')
print()

# Print n lines of increasing stars
for i in range(0, number_of_stars):
    for j in range(0, i + 1):
        print("* ", end="")
    print()
