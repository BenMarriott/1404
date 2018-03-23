"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    monthly_income = int(input("Enter number of incomes to report: "))

    for i in range(monthly_income):
        income = float(input("Enter number of income for month {}: ".format(i + 1)))
        incomes.append(income)

    print("\n Income Report\n" + ("-" * 20))

    def print_report():
        total = 0
        for month in range(1, monthly_income + 1):
            income = incomes[month - 1]
            total += income
            print(" Month {:2} - Income: $ {:<10.2f} Total: $ {:10.2f}".format(monthly_income, month, total))
            # TODO does not print correct month.
    print_report()


main()
