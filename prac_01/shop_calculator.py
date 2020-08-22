"""program to work out the total price for a number of items, each with different prices."""

number_of_items = int(input("Number of items: "))
while number_of_items < 0:  # error checking
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

total_price = 0  # input price of item and calculate total
for i in range(number_of_items):
    price_of_item = float(input("Price of item: "))
    total_price += price_of_item

if total_price > 100:  # determine discount and print total
    discount = total_price * 0.1
    discounted_price = total_price - discount
    print(f"Total price for {number_of_items} items is ${discounted_price:.2f}")
else:
    print(f"Total price for {number_of_items} items is ${total_price:.2f}")
