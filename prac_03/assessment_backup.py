"""
Ben Marriott, 18/03/18, <brief program details here><link to github program here>.
"""


def main():
    print("Movies To Watch 1.0 - by Ben Marriott \n <see TODO>")

    get_choice = input("Menu: \n L - List movies \n A - Add new movie \n W - Watch a movie \n "
                       "Q - Quit \n >>>").capitalize()

    while get_choice != "Q":
        if get_choice == "L":
            print('list movies')
        elif get_choice == "A":
            print("add movie")
        elif get_choice == "W":
            print("watch movie")
        else:
            get_choice = print("Invalid menu choice \n {}".format(get_choice))


if __name__ == '__main__':
    main()
