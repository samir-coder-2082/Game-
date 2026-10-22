import tkinter as tk

score = 0

def tap():
    global score
    score += 1
    label.config(text=f"Score: {score}")

def reset():
    global score
    score = 0
    label.config(text="Score: 0")

root = tk.Tk()
root.title("My First Game")
root.geometry("350x450")
root.configure(bg="#151515")

title = tk.Label(
    root,
    text="TAP COUNTER GAME",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="#151515"
)
title.pack(pady=35)

label = tk.Label(
    root,
    text="Score: 0",
    font=("Arial", 30),
    fg="yellow",
    bg="#151515"
)
label.pack(pady=25)

tap_button = tk.Button(
    root,
    text="TAP ME!",
    font=("Arial", 22, "bold"),
    bg="#00cc66",
    command=tap
)
tap_button.pack(pady=20)

reset_button = tk.Button(
    root,
    text="RESET",
    font=("Arial", 16),
    bg="orange",
    command=reset
)
reset_button.pack(pady=15)

root.mainloop()
