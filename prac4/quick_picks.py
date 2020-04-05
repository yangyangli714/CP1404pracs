"""
CP1404 Practical
"""

import random

minimum = 1
maximum = 45
number_per_line = 6

# ask for number of lines
number_of_quick_picks = int(input("How many quick picks? "))

# start to generate the lines
for i in range(number_of_quick_picks):
    quick_pick = []
    # generate the number in one line
    for j in range(number_per_line):
        number = random.randint(minimum, maximum)
        # avoiding any repeated numbers
        while number in quick_pick:
            number = random.randint(minimum, maximum)
        quick_pick.append(number)
    # display the number in ascending order
    quick_pick.sort()
# print the output
    print(" ".join("{:2}".format(number) for number in quick_pick))


