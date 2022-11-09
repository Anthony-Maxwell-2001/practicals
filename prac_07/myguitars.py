"""
CP1404 myguitars.py

Anthony Maxwell
"""
import csv
from prac_06.guitar import Guitar


def main():
    guitars = []

    in_file = open("guitars.csv", 'r')
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()

    guitars.sort()
    for guitar in guitars:
        print(guitar)


main()


