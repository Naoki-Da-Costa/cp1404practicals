"""
CP1404/CP5632 - Practical
Gets integer from user and does not crash when a non-number is entered
"""

finished = False
result = 0
while not finished:
    try:
        result = int(input("Enter an integer: "))
        finished = True
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)
