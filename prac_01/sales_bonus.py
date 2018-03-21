"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

def main():

    sales = float(input("Enter sales: $"))
    test_variable = 0
    while sales > (test_variable)-1:
        if sales >= 1000:
            print("You get a bonus of 15%, which is: $",sales/100 * 15)
        else:
            print("You get a bonus of 10%, which is: $", sales/100 * 10)
        sales = float(input("Enter sales: $"))
    print("Cannot accept negative")

main()
