def main():
    incomes = []

    income_months = int(input("Enter number of incomes to report: "))

    # while amount_incomes >= 0:
    for i in range(income_months):
        income = int(input("Enter number of income for month {}: ".format(i + 1)))
        incomes.append(income)

    print("\n Income Report\n" + ("-" * 20))

    def print_report():
        global income
        total = 0
        for element in incomes:
            income = incomes[income_months - 1]
            total += income
            print(" Month {} - Income: $ {} Total: $ {}".format(income_months, element, total))


    print_report()

main()
