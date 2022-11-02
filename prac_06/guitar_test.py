"""
CP1404 guitar_test.py
By Anthony Maxwell
"""

from prac_06.guitar import Guitar


def run_tests():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    other_guitar = Guitar("Another Guitar", 2010, 16035.40)

    print(f"{guitar.name} get_age() - expected 100. got {guitar.get_age()}")
    print(f"{other_guitar.name} get_age() - expected 12. got {other_guitar.get_age()}")
    print(f"{guitar.name} is_valid() - expected True got {guitar.is_vintage()}")
    print(f"{other_guitar.name} is_valid() - expected False got {other_guitar.is_vintage()}")


if __name__ == '__main__':
    run_tests()
