"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""
import string
MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid Password.\nYour password must be between {0} and {1} characters and contain: \n\t{2}"
          " or more uppercase characters\n\t{2} or more lowercase characters\n\t{2} or more numbers".format(MIN_LENGTH, MAX_LENGTH, 1))
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ".format(SPECIAL_CHARACTERS))
    password = input(str("> "))
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password),
                                                           password))


def is_valid_password(password):
    """Determine if the provided password is valid."""
    # TODO: if length is wrong, return False
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH: #Does not account for Min
        print(type(len(password)))
        return False
    #Count different types
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        elif char.isdigit():
            count_digit += 1
        elif char in SPECIAL_CHARACTERS:
            count_special += 1

    if count_upper == 0 or count_lower == 0 or count_digit == 0:
        return False

    if SPECIAL_CHARACTERS:
        if count_special == 0:
            return False
    return True


main()