"""
CP1404/CP5632 - Practical

"""

name = input("Enter Name: ")

print("(H)ello\n(G)oodbye\n(Q)uit")
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid Choice")
    print("(H)ello\n(G)oodbye\n(Q)uit")
    choice = input(">>> ").upper()
print("Finished.")
