"""CP1404 Practical - Scores.py"""

score = float(input("Enter score: "))
if score >= 0 and score <= 100:
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")
else:
    print("invalid score")
