import speech_recognition as sr
import requests
import webbrowser
import os

recognizer = sr.Recognizer()

def capture_voice_input():
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            print("Audio captured successfully.")
        except sr.WaitTimeoutError:
            print("Listening timed out.")
            return None
        except sr.RequestError as e:
            print(f"Error accessing the microphone: {e}")
            return None
    return audio

def convert_voice_to_text(audio):
    if audio is None:
        return ""
    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        text = ""
        print("Sorry, I didn't understand that.")
    except sr.RequestError as e:
        text = ""
        print(f"Error; {e}")
    return text

def search_web(query):
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)
    print(f"Searching for {query} on Google.")

def process_voice_command(text):
    if "hello" in text.lower():
        print("Hello! How can I help you?")
    elif "goodbye" in text.lower():
        print("Goodbye! Have a great day!")
        return True
    elif "search for" in text.lower():
        query = text.lower().split("search for")[-1].strip()
        search_web(query)
    else:
        print("I didn't understand that command. Please try again.")
    return False

def main():
    end_program = False
    while not end_program:
        audio = capture_voice_input()
        text = convert_voice_to_text(audio)
        end_program = process_voice_command(text)

if __name__ == "__main__":
    main()
