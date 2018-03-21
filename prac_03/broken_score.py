def main():
    print(get_score())


def get_score():
    score = float(input("Enter score: "))
    while 0 > score > 100:
        float(input("Invalid number - please re-enter: "))
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"


main()
