"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    result = determine_score(score)
    print(result)


def random_score():
    score = random.randint(0, 101)
    result = determine_score(score)
    print(result)


def determine_score(score):
    if 0 <= score <= 100:
        if score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Passable"
        elif score >= 0:
            return "Bad"
    else:
        return "Invalid score"


# main()
random_score()
