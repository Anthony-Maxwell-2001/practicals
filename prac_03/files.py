
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

# Program 3:
in_file = open("numbers.txt", 'r')
first_number = int(in_file.readline())
second_number = int(in_file.readline())
print(first_number + second_number)
in_file.close()

in_file = open("numbers.txt", 'r')
total_number = 0
for line in in_file:
    number = int(line)
    total_number += number
print(total_number)
in_file.close()


