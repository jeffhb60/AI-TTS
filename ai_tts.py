import os
from gtts import gTTS
# from playsound import playsound
import pygame
# import pyttsx3

con_prog = True

while con_prog:
    txt = input("Please enter some text to output to a file: ")

    # Remove cost calculation if using a free service
    # cost = len(txt)/1000 * 0.15
    # print("Having this converted to speech will cost about ${:.2f}.".format(cost))

    con = input("Would you like to continue (Y/N)? ")

    while con.upper() != "Y" and con.upper() != "N":
        print("Invalid choice. Please try again.")
        con = input("Would you like to continue (Y/N)? ")

    f = input("Enter the filename: ")
    if con.upper() == "Y":
        try:
            tts = gTTS(text=txt, lang="en", slow=False)

            tts.save("sound/" + f + ".mp3")
            print("MP3 file created successfully.")

            play = input("Would you like to play the audio now? (Y/N): ")
            if play.upper() == "Y":
                try:
                    pygame.mixer.init()
                    pygame.mixer.music.load("sound/" + f + ".mp3")
                    pygame.mixer.music.play()
                    print("Playing audio...")
                    # Keep the script running until playback finishes
                    while pygame.mixer.music.get_busy():
                        pygame.time.Clock().tick(10)
                except Exception as e:
                    print(f"An error occurred while playing audio: {e}")
                finally:
                    pygame.mixer.music.unload()
        except Exception as e:
            print(f"An error occurred: {e}")

    elif con.upper() == "N":
        print("Thank you for using AI-TTS! No file was created.")

    again = input("Would you like to create another voice sound? (Y/N): ").strip().upper()

    while again != "Y" and again != "N":
        print("Invalid choice. Please try again.")
        again = input("Would you like to create another voice sound? (Y/N): ").strip().upper()

    if again == "N":
        con_prog = False
        print("Goodbye!")