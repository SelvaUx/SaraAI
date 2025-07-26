import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init()

# Adjusting the properties for a more professional tone
engine.setProperty('rate', 160)  # Speed of speech
engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)
voices = engine.getProperty('voices')
if len(voices) > 1:
    engine.setProperty('voice', voices[1].id)  # Female voice (use index 0 for male voice)
else:
    engine.setProperty('voice', voices[0].id)

def speak(text: str) -> None:
    """Converts text to speech with a dynamic tone."""
    engine.say(text)
    engine.runAndWait()
