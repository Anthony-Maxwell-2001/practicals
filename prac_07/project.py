"""
CP1404 projects.py

Estimate: 3 hours
Actual:
"""


class Project:
    def __init__(self, project_name, start_date, priority, cost_estimate, completion_percentage):
        self.project_name = project_name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return f"{self.project_name}, start: {self.start_date}, priority {self.priority}," \
               f" estimate: ${self.cost_estimate}, completion: {self.completion_percentage}%"
