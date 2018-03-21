get_name = input("enter name")
menu_choice = input("""Please choose:
 (H)ello
 (G)oodbye
 (Quit)""").upper()
while menu_choice != "Q":
    if menu_choice == "H":
        print("Hello", get_name)
    elif menu_choice == "G":
        print("Goodbye", get_name)
    else:
        print("Wrong")
    menu_choice = input("""Please choose:
 (H)ello
 (G)oodbye
 (Quit)""")
print("Catch ya")

