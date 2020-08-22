# Displays all of the odd numbers between 1 and 20
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

# Ask the user for a number, then print that many stars
number = int(input("Number of stars: "))
print(number * "*")

# Using the same number print n lines of increasing stars starting at 1
for i in range(1, number+1):
    print(i * "*")
