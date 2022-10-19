COLOUR_TO_HEX = {"purple": "#a020f0", "yellow1": "#ffff00", "orangered1": "#ff4500", "opal": "#a8c3bc",
                 "mint": "#3eb489", "light": "#eedd82", "gold1": "#ffd700", "darkorchid": "#9932cc",
                 "azure1": "#f0ffff", "amethyst": "#9966cc"}
print(COLOUR_TO_HEX)

colour = input("Enter colour name: ")
while colour != "":
    if colour in COLOUR_TO_HEX:
        print(colour, "is", COLOUR_TO_HEX[colour])
    else:
        print("Invalid colour")
    colour = input("Enter colour name: ")
