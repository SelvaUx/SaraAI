
import speech_recognition as sr
from tts import speak

WAKE_WORD = "hey sara"

def listen_for_command() -> str:
    try:
        recognizer = sr.Recognizer()
        mic = sr.Microphone()
    except Exception as e:
        print(f"Microphone or PyAudio error: {e}")
        speak("Sorry, I couldn't access the microphone.")
        return ""

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("🎤 Waiting for wake word: 'Hey Sara'...")

        while True:
            try:
                audio = recognizer.listen(source)
                query = recognizer.recognize_google(audio).lower()
                print(f"🔊 Heard: {query}")

                if WAKE_WORD in query:
                    speak("Yes, I'm listening.")
                    print("🎧 Wake word detected. Listening for command...")

                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio).lower()
                    print(f"🗣️ Command received: {command}")
                    return command
            except sr.UnknownValueError:
                continue
            except sr.RequestError:
                speak("Sorry, my speech service is down.")
                return ""
