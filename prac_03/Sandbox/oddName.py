"""Ben Marriott"""

name = input("Enter name: ")

while name == "":
    name = input("Re-enter valid name: ")
print(name[1::2])
