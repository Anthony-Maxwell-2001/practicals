"""CP-1404 Practical"""

MENU = """[E]nter Valid Score
[C]heck Score
[P]rint Stars
[Q]uit"""


def main():
    print(MENU)
    score = 0
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "E":
            score = get_valid_score()
        elif choice == "C":
            result = check_score(score)
            print(result)
        elif choice == "P":
            print_stars(score)
        else:
            print("Invalid Option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell.")


def print_stars(score):
    print(score * "*")


def check_score(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def get_valid_score():
    score = int(input("Enter score between 0 and 100: "))
    while score > 100 or score < 0:
        print("Invalid Score")
        score = int(input("Enter score: "))
    return score


main()
