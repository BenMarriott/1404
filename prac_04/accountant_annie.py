"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_incomes = int(input("Enter number of incomes to report: "))

    for i in range(number_incomes):
        income = float(input("Enter number of income for month {}: ".format(i + 1)))
        incomes.append(income)
    print("\n Income Report\n" + ("-" * 20))
    print_report(number_incomes, incomes)


def print_report(number_incomes, incomes):
    total = 0
    for month_number in range(1, number_incomes + 1):
        income = incomes[month_number - 1]
        total += income
        print(" Month {:2} - Income: $ {:<10.2f} Total: $ {:10.2f}".format(month_number, income, total))
        # TODO does not print correct month_number.


main()
