import pyttsx3
import logging

# Suppress the logging from comtypes to avoid the 'NoneType' errors
logging.basicConfig(level=logging.CRITICAL)

# Initialize the TTS engine
engine = pyttsx3.init()

def list_voices():
    # Get and list all available voices
    voices = engine.getProperty('voices')
    for index, voice in enumerate(voices):
        print(f"{index}: {voice.name} ({voice.languages}) - {voice.gender}")
    return voices

def set_voice(voice_id):
    # Set the voice for the engine
    engine.setProperty('voice', voice_id)

def set_speech_rate(rate):
    # Set the speech rate (words per minute)
    engine.setProperty('rate', rate)

def speak_text(text):
    try:
        # Speak the provided text
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # List available voices
    voices = list_voices()

    # Ask the user to select a voice
    choice = int(input("Select a voice by number: "))
    selected_voice = voices[choice].id
    set_voice(selected_voice)

    # Ask the user to input the text they want to convert to speech
    text = input("Enter the text to convert to speech: ")

    # Optional: Set speech rate (default is around 200 words per minute)
    rate = input("Enter speech rate (default 200, higher is faster, lower is slower): ")
    if rate:
        set_speech_rate(int(rate))

    # Convert text to speech
    speak_text(text)

if __name__ == "__main__":
    main()
