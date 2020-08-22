# Write code that asks the user for their name, then opens
# a file called "name.txt" and writes that name to it.
out_file = open("name.txt", "w")
name = input("Name: ")
print(name, file=out_file)
out_file.close()

# Write code that opens "name.txt" and reads the name (as above) then prints,
# "Your name is Bob" (or whatever the name is in the file).
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Your name is {name}")

# Write code that opens "numbers.txt", reads only the first
# two numbers and adds them together then prints the result.
in_file = open("numbers.txt", "r")
number_1 = int(in_file.readline())
number_2 = int(in_file.readline())
print(number_1 + number_2)

# Write a fourth block of code that prints the total for all
# lines in numbers.txt or a file with any number of numbers.
total = 0
in_file = open("numbers.txt", "r")
for line in in_file:
    total += 1
in_file.close()
print(total)
