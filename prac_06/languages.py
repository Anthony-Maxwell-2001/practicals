"""
CP1401 languages.py
By Anthony Maxwell

Estimate: 20 minutes
Actual: 12 minutes
"""

from prac_06.programming_language import ProgrammingLanguage
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

languages = [python, ruby, visual_basic]
print("The Dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.name)
