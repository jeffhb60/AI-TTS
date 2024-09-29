import os
from gtts import gTTS
from playsound import playsound


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
        # Create the TTS object
        tts = gTTS(text=txt, lang='en', slow=False)

        # Save the audio file
        tts.save("sound/"+f+".mp3")
        print("MP3 file created successfully.")

        print("Your file has been downloaded!")
    except Exception as e:
        print(f"An error occurred: {e}")

elif con.upper() == "N":
    print("Thank you for using AI-TTS! No file was created.")

