# TODO: Reformat this file so the dictionary code follows PEP 8 convention
COLOUR_NAMES = {"AliceBlue": "#f0f8ff", "blue1": "#0000ff", "black": "#000000", "blue2": "0000ee",
                "azure2": "e0eeee", "azure3": "c1cdcd", "cornsilk2": "#eee8cd", "cyan1": "#00ffff",
                "DarkGreen": "#006400"}
# print(STATE_NAMES)

colour_name = input("Enter the name of your colour: ")
while colour_name != "":
    print("The hexadecimal code for {} is {}".format(colour_name, COLOUR_NAMES[colour_name]))
    colour_name = input("Enter the name of your colour: ")
