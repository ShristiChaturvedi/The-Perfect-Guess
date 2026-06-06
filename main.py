import tkinter as tk
from tkinter import messagebox
import random
import pyttsx3

# Initialize voice engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Generate random number
random_number = random.randint(1, 100)
attempts = 0

def check_guess():
    global attempts

    try:
        guess = int(entry.get())
        attempts += 1

        if guess < random_number:
            result_label.config(text="⬆️ Too Low! Try Higher.")
            speak("Too low. Try a higher number.")
        elif guess > random_number:
            result_label.config(text="⬇️ Too High! Try Lower.")
            speak("Too high. Try a lower number.")
        else:
            result_label.config(
                text=f"🎉 Correct! Attempts: {attempts}"
            )
            speak(
                f"Congratulations! You guessed the number in {attempts} attempts."
            )
            messagebox.showinfo(
                "Winner",
                f"You guessed the number in {attempts} attempts!"
            )

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")
        speak("Please enter a valid number.")

# GUI Window
root = tk.Tk()
root.title("The Perfect Guess")
root.geometry("450x300")

title = tk.Label(
    root,
    text="🎯 The Perfect Guess",
    font=("Arial", 18, "bold")
)
title.pack(pady=15)

instruction = tk.Label(
    root,
    text="Guess a number between 1 and 100"
)
instruction.pack()

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

guess_btn = tk.Button(
    root,
    text="Guess",
    command=check_guess,
    font=("Arial", 12)
)
guess_btn.pack()

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 12)
)
result_label.pack(pady=20)

speak("Welcome to The Perfect Guess Game")

root.mainloop()