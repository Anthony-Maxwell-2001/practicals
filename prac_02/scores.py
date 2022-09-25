"""CP1404 Practical - Scores.py"""

from random import randint


def main():
    user_score = float(input("Enter your score: "))
    user_result = calculate_results(user_score)
    print("Your score is: ", user_result)
    random_score = randint(0, 100)
    random_result = calculate_results(random_score)
    print(f"Random score is: {random_score} it is: {random_result}")


def calculate_results(score):
    if score >= 0 and score <= 100:
        if score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Passable"
        else:
            return "Bad"
    else:
        return "Invalid Score"
    pass


main()
