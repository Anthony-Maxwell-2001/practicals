"""
CP1404/CP5632 - Practical
The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total before the amount is displayed on the
screen.
"""

total_item_price = 0

number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

for item_number in range(number_of_items):
    price_of_item = float(input("Price of Item: "))
    total_item_price = total_item_price + price_of_item

if total_item_price > 100:
    total_item_price = total_item_price * 0.9

print("Total price for {} is {:.2f}".format(number_of_items, total_item_price))
