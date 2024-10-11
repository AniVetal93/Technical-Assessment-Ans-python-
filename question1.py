#You are tasked with developing a Python program to suggest search query completions based on a user's search history. The program should efficiently find completions using a any search algorithm

def get_search_suggestions(search_history, query):
    # Normalize the query to lowercase for case-insensitive matching
    query = query.lower()
    suggestions = []

    for item in search_history:
        if item.lower().startswith(query):
            suggestions.append(item)

    return suggestions

# Input
search_history = [
    "apple",
    "banana",
    "carrot",
    "pear",
    "pineapple",
    "potato",
    "strawberry"
]

# User input
query = input("Enter your partial search query: ").strip()
suggestions = get_search_suggestions(search_history, query)

# Output suggestions
if suggestions:
    print("Suggestions:")
    for suggestion in suggestions:
        print(suggestion)
else:
    print("No suggestions found.")
