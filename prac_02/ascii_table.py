LOWER = 33
UPPER = 127

users_character = input("Enter a character: ")
users_int = ord(users_character)
while LOWER <= users_int and UPPER >= users_int:
    print(users_int)

