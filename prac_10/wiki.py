import wikipedia

user_summary = input("Enter a page to get a summary for: ")
while user_summary != '':
    try:
        page = wikipedia.page(user_summary, auto_suggest=False)
        print(f"{page.title}\n{page.url}")
        print(wikipedia.summary(user_summary, auto_suggest=False))
    except wikipedia.exceptions.DisambiguationError as error:
        print(error.options)
    user_summary = input("Enter a page to get a summary for: ")
