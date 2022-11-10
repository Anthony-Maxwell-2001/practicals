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
            pass
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


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
