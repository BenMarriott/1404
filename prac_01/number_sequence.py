#x, y = int(input("Enter first number: ")), int(input("Enter second number: "))
#print(type(x), type(y))
#for x in range(y):

#menu_choice = "Q"
#while menu_choice != "Q":

menu_choice = input("Would you like to run the program?:" "\n" "(Y)es or (Q)uit")
while menu_choice != "Q":
    y = int(input("Enter second number: "))
    x = int(input("Enter first number: "))
    is_it_even = x % 2
    is_it_odd = y % 2
    
    if is_it_even == 0:
        print("even")
    elif is_it_even == 1:
        print("odd")
    menu_choice = input("Would you like to run the program?:" "\n" "(Y)es or (Q)uit")
print("made it thru")

