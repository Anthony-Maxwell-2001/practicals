"""
CP1404 Guitars.py
By Anthony Maxwell
"""

from prac_06.guitar import Guitar


def main():
    guitars = []

    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    for i, guitar in enumerate(guitars, 1):
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = " (vintage)"
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


main()
