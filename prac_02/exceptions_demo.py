try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")


# When will a ValueError occur?
# When the input is not a number

# When will a ZeroDivisionError occur?
# When the denominator is 0

# Could you change the code to avoid the possibility of a ZeroDivisionError?
# Yes by asking the user for a number until they enter a number higher than zero for the denominator
