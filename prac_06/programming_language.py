"""
CP1401 programming_languages.py
By Anthony Maxwell

Estimate: 20 minutes
Actual: 12 minutes
"""


class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.typing}, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        return self.typing == "Dynamic"
