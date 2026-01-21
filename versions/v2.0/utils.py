import wikipedia
import datetime
import pyjokes

def search_wikipedia(query: str) -> str:
    """Searches Wikipedia and returns a summary."""
    try:
        result = wikipedia.summary(query, sentences=2)  # Fetch a brief summary
        return result
    except wikipedia.exceptions.DisambiguationError:
        return "Multiple results found. Please be more specific."
    except Exception as e:
        return f"I couldn't find anything on Wikipedia. Error: {e}"

def time() -> str:
    """Returns the current time as a string."""
    current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
    return f"The current time is {current_time}"

def date() -> str:
    """Returns the current date as a string."""
    now = datetime.datetime.now()
    return f"The current date is {now.day}/{now.month}/{now.year}"

def joke() -> str:
    """Returns a random joke."""
    return pyjokes.get_joke()
