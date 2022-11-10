"""
CP1404 project_management.py

Estimate: 3 hours
actual:
"""
from project import Project
import datetime
from operator import attrgetter

MENU = """(L)oad projects
(S)ave projects
(D)isplay projects
(F)ilter projects by date
(A)dd new project
(U)pdate project
(Q)uit"""


def main():
    projects = []
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            load_projects_from_file(projects)
        elif choice == "S":
            save_to_file(projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            display_projects_filtered_by_date(projects)
        elif choice == "A":
            add_new_project(projects)
        elif choice == "U":
            update_projects(projects)

        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


def display_projects_filtered_by_date(projects):
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    projects.sort(key=attrgetter('start_date'))
    for project in projects:
        if project.start_date > date:
            print(project)


def save_to_file(projects):
    file_name = input("Filename: ")
    with open(file_name, 'w') as in_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=in_file)
        for project in projects:
            print(project, file=in_file)
            # Could not figure out a way to write this to a file in the original formatting


def update_projects(projects):
    for i, project in enumerate(projects):
        i += 0
        print(i, project)
    project_to_modify = get_valid_number("Project choice: ", projects)
    print(projects[project_to_modify])
    new_percentage = int(input("New Percentage: "))
    if new_percentage != "":
        projects[project_to_modify].completion_percentage = new_percentage
    new_priority = int(input("New Priority: "))
    if new_priority != "":
        projects[project_to_modify].priority = new_priority
    return projects


def get_valid_number(user_input, projects):
    """Gets a valid number and returns it"""
    valid_number = False
    while not valid_number:
        try:
            number = int(input(user_input))
            if len(projects) <= number <= -1:
                print("Number must be within numbers listed above")
            else:
                valid_number = True
                return number
        except ValueError:
            print("Invalid input; enter a valid number")


def add_new_project(projects):
    print("Lets add a new project: ")
    name = input("Name: ")
    date_string = input("Start date (dd/mm/yy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    priority = input("Priority: ")
    cost = float(input("Cost Estimate: $"))
    completion = int(input("Percent completed: "))
    project_to_add = Project(name, date, priority, cost, completion)
    projects.append(project_to_add)
    return projects


def display_projects(projects):
    print("Incomplete Projects:")
    projects.sort(key=attrgetter('priority'))
    for project in projects:
        if project.completion_percentage < 100:
            print(project)
    print("Completed Projects:")
    for project in projects:
        if project.completion_percentage == 100:
            print(project)


def load_projects_from_file(projects):
    file_name = input("Filename: ")
    with open(file_name, 'r') as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            date_string = parts[1]
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            project = Project(parts[0], date, parts[2], parts[3], int(parts[4]))
            projects.append(project)
    return projects


main()
