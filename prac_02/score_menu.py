

def main():
    pass


def get_valid_score():
    score = int(input("Enter score: "))
    while score > 100 or score < 0:
        print("x")
        score = int(input("Enter score: "))
    return score


main()

