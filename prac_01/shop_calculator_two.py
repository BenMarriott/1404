number_of_items = int(input("Please enter number of items: "))
while number_of_items <= 0:
    number_of_items = int(input("Invalid number of items! Please re-enter: "))


total_price = 0
for i in range(number_of_items):
    item_price = float(input("Please enter the item's cost: "))
    total_price += item_price
if total_price > 100:
    total_price *= 0.9


print("Total price for", number_of_items, "items is ${:.2f}".format(total_price))

