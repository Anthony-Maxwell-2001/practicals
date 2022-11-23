"""
CP1404 myguitars.py

Anthony Maxwell
"""
import csv
from prac_06.guitar import Guitar


def main():
    guitars = []
    get_guitars_from_file(guitars)
    get_new_guitar(guitars)
    display_guitars(guitars)
    save_to_file(guitars)


def get_guitars_from_file(guitars):
    """Save the guitars to a list from the CSV file."""
    in_file = open("guitars.csv", 'r')
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()


def display_guitars(guitars):
    """Displays the guitars."""
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def get_new_guitar(guitars):
    """Adds a new guitar to the list"""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        name = input("Name: ")


def save_to_file(guitars):
    """Saves the list of guitars to a file"""
    with open("guitars.csv", 'w') as out_file:
        for guitar in guitars:
            print(repr(guitar), file=out_file)


main()
