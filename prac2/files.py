"""
CP1404/CP5632 - Practical
Write code that asks the user for their name, then opens a file called "name.txt"
"""

new_file = open("name.txt", "w")
name = input("What is your name? ")
print(name, file=new_file)
new_file.close()

open_file = open("name.txt", "r")
name = open_file.read().strip()
open_file.close()
print("Your name is", name)




open_file = open("numbers.txt", "r")
line1 = int(open_file.readline())
line2 = int(open_file.readline())
open_file.close()
print(line1 + line2)

open_file = open("numbers.txt", "r")
line1 = int(open_file.readline())
line2 = int(open_file.readline())
line3 = int(open_file.readline())
open_file.close()
print(line1, line2, line3)
