from random import randint

NUMBERS_PER_LINES = 6
MINIMUM = 1
MAXIMUM = 45

def main():
    """Quick pick program - Prints sets of random numbers"""
    number_of_quick_picks = int(input("How many quick pick numbers? "))
    while number_of_quick_picks < 0:
        number_of_quick_picks = int(input("Please choose a valid input\nHow many quick pick numbers? "))

    for i in range(number_of_quick_picks):
        quick_pick = []
        for number in range(NUMBERS_PER_LINES):
            number = randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()
        print((" ".join("{:2}".format(number) for number in quick_pick)))



main()