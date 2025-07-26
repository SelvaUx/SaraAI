import webbrowser, pyautogui, time, urllib.parse

def open_google_search(query: str):
    url = f"https://www.google.com/search?q={urllib.parse.quote(query)}"
    webbrowser.open(url)
    print(f"Searching Google for {query}")

def youtube_search(query: str):
    url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(query)}"
    webbrowser.open(url)
    time.sleep(3)
    # optional: auto-click first video
    pyautogui.click(x=450, y=350)   # adjust coordinates for your screen
    print("YouTube search started")

def handle_browser_commands(command: str):
    if "search" in command.lower():
        q = command.replace("search", "").strip()
        if q: open_google_search(q)
    elif "open" in command.lower():
        app = command.replace("open", "").strip().lower()
        from application_handler import open_application
        open_application(app)