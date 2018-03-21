TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

tariff_selection = input("Which tariff?")
if tariff_selection == 11:
    tariff_selection = TARIFF_11
elif tariff_selection == 31:
    tariff_selection = TARIFF_31
else:
    print("wrong")

    daily_kWh_consumption = float(input("Enter daily kWh consumption: "))
    billing_period = int(input("Enter your billing period in days: "))

    print("Estimated bill: ", (int(tariff_selection)/int(daily_kWh_consumption) * billing_period ))