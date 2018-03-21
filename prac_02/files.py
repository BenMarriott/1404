# names_file = open("name.txt", "w")  # Opens txt file
# users_name = input("Please enter your name")
# print(users_name, file=names_file)  # Stores varibabele in txt file
# names_file.close()  # Closes txt file

# names_file = open("name.txt", "r")
# print(names_file.read())  # Reads from txt file
# names_file.close()
#
numbers_file = open("numbers.txt", "w")  # Opens txt file
print("17\n42", file=numbers_file)  # Stores 17 & 42 in txt AS STR
numbers_file.close()

#
numbers_file = open("numbers.txt", "r")
print(numbers_file.readline())  # TODO convert to int to add both values together use ord()??
