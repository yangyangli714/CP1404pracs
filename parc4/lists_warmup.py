"""
CP1404 Practical
"""


numbers = [3, 1, 4, 1, 5, 9, 2]

# Questions that asked on the prac sheet with solutions
"""
- numbers[0]
3 correct
- numbers[-1]
2 correct
- numbers[3]
1 correct
- numbers[:-1]
[3, 1, 4, 1, 5, 9, 2] wrong,    [3]
- numbers[3:4]
1 wrong, [1]
- 5 in numbers
ture correct
- 7 in numbers
false correct
- "3" in numbers
false correct
- numbers + [6, 5, 3]
[3, 1, 4, 1, 5, 9, 2, 6, 5, 3] correct
"""


# Change the first element of numbers to "ten" (the string, not the number 10)
numbers[0] = "ten"
print(numbers)
# Change the last element of numbers to 1
numbers[-1] = 1
print(numbers)
# Get all the elements from numbers except the first two (slice)
print(numbers[2:])
# Check if 9 is an element of numbers
test = 9 in numbers
print(test)
