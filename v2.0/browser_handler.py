import webbrowser
from application_handler import open_application  # Importing the function to open applications

def open_google_search(query: str) -> None:
    """Opens a search query in Google using the default browser."""
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)
    print(f"Searching for '{query}' in the default browser.")

def handle_browser_commands(command: str) -> None:
    """Handles user commands for browsing and opening applications."""
    if "search" in command.lower():
        query = command.replace("search", "").strip()  # Extract search term
        if query:
            open_google_search(query)
        else:
            print("Please specify a search term after 'search'.")
    elif "open" in command.lower():
        # Handle opening applications via Windows Search
        app_name = command.replace("open", "").strip().lower()
        open_application(app_name)
    else:
        print("Invalid command. Use 'search [query]' or 'open [application]'.")
