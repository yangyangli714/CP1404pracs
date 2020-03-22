"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    print(result_status(score))
    random_score = random.randint(1, 101)
    print(random_score)
    print(random_status(random_score))

def result_status(score):
    if 0 < score > 100:
        return "Invalid score"

    elif score >= 90:
        return "Excellent"

    elif score >= 50:
        return "Passable"

    else:
        return "Bad"


def random_status(random_score):
    if 0 < random_score > 100:
        return "Invalid score"

    elif random_score >= 90:
        return "Excellent"

    elif random_score >= 50:
        return "Passable"

    else:
        return "Bad"

main()
