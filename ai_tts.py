import os
import tkinter as tk
from tkinter import messagebox
from gtts import gTTS
import pygame
import threading

# Initialize pygame mixer
pygame.mixer.init()

# Create main window
root = tk.Tk()
root.title("AI-TTS Text-to-Speech")
root.geometry("500x400")


# Function to create the MP3 file
def create_mp3():
    text = text_entry.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Input Error", "Please enter some text.")
        return

    filename = filename_entry.get().strip()
    if not filename:
        messagebox.showwarning("Input Error", "Please enter a filename.")
        return

    # Ensure 'sound' directory exists
    if not os.path.exists("sound"):
        os.makedirs("sound")

    filepath = os.path.join("sound", filename + ".mp3")
    try:
        tts = gTTS(text=text, lang="en", slow=False)
        tts.save(filepath)
        messagebox.showinfo("Success", f"MP3 file '{filename}.mp3' created successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


# Function to play the MP3 file
def play_mp3():
    filename = filename_entry.get().strip()
    if not filename:
        messagebox.showwarning("Input Error", "Please enter a filename to play.")
        return

    filepath = os.path.join("sound", filename + ".mp3")
    if not os.path.exists(filepath):
        messagebox.showwarning("File Not Found", f"The file '{filename}.mp3' does not exist.")
        return

    try:
        pygame.mixer.music.load(filepath)
        pygame.mixer.music.play()
        # Run a separate thread to monitor playback
        threading.Thread(target=check_playback, daemon=True).start()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while playing audio: {e}")


def check_playback():
    while pygame.mixer.music.get_busy():
        pass
    pygame.mixer.music.unload()
    messagebox.showinfo("Playback Finished", "Audio playback has finished.")


# Function to reset the fields
def reset_fields():
    text_entry.delete("1.0", tk.END)
    filename_entry.delete(0, tk.END)


# Function to exit the application
def exit_app():
    root.destroy()


# GUI Elements
text_label = tk.Label(root, text="Enter text to convert to speech:")
text_label.pack(pady=5)
text_entry = tk.Text(root, height=5, width=60)
text_entry.pack(pady=5)

filename_label = tk.Label(root, text="Enter filename (without extension):")
filename_label.pack(pady=5)
filename_entry = tk.Entry(root, width=50)
filename_entry.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

create_button = tk.Button(button_frame, text="Create MP3 File", command=create_mp3)
create_button.grid(row=0, column=0, padx=5)

play_button = tk.Button(button_frame, text="Play MP3 File", command=play_mp3)
play_button.grid(row=0, column=1, padx=5)

reset_button = tk.Button(button_frame, text="Reset", command=reset_fields)
reset_button.grid(row=0, column=2, padx=5)

exit_button = tk.Button(button_frame, text="Exit", command=exit_app)
exit_button.grid(row=0, column=3, padx=5)

# Start the main loop
root.mainloop()
