
# Program 1:
name = input("Name: ")
out_file = open("name.txt", 'w')
print(name, file=out_file)
out_file.close()

# Program 2:
in_file = open("name.txt", 'r')
name = in_file.read()
print(f"Your name is {name}")
in_file.close()
