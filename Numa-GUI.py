import random
import tkinter as tk
from tkinter import messagebox, simpledialog

# Minimal copy of resources from Numa.py
affirmations_motivational = [
    "You are capable of amazing things.",
    "Every day is a new beginning.",
    "You are stronger than you think."
]

affirmations_soothing = [
    "Breathe in calm, breathe out stress.",
    "You deserve kindness and peace.",
    "Let go of what you cannot control."
]

calming_tips = [
    "Try breathing exercises for 3 minutes. 🌬️",
    "Take a short walk outside and enjoy nature. 🌳",
    "Listen to calming music or your favorite song. 🎵"
]

urgent_keywords = {"hurt", "suicide", "depressed", "sad", "lonely", "anxious"}
mood_history = []

def detect_urgent_keywords(text):
    if not text:
        return False
    lower = text.lower()
    if any(k in lower for k in urgent_keywords):
        messagebox.showwarning("If you're in crisis",
                               "If you are feeling overwhelmed, consider talking to a trusted person or a professional helpline.")
        return True
    return False

def start_session():
    anon = anon_var.get() == 1
    name = "Friend" if anon else (name_var.get().strip() or "Friend")
    style = style_var.get()  # 1 motivational, 2 soothing
    want_reminder = reminder_var.get() == 1

    if want_reminder:
        aff = random.choice(affirmations_motivational if style == 1 else affirmations_soothing)
        messagebox.showinfo("Daily reminder", aff)

    # Ask mood
    mood = simpledialog.askinteger("Mood", "On a scale of 1 (worst) to 5 (best), how are you feeling right now?", minvalue=1, maxvalue=5)
    if mood is None:
        return
    mood_history.append(mood)

    highlight = simpledialog.askstring("Good thing", "What's one good thing that happened today?")
    detect_urgent_keywords(highlight)

    worry = simpledialog.askstring("Bothering you?", "Is there something bothering you that you'd like to share?")
    detect_urgent_keywords(worry)

    # personalized response
    if style == 1:
        aff_list = affirmations_motivational
    else:
        aff_list = affirmations_soothing

    if mood <= 2:
        tip = random.choice(calming_tips)
        messagebox.showinfo("Support", f"{name}, it seems you've had a tough day.\n\nTip: {tip}")
    elif mood == 3:
        aff = random.choice(aff_list)
        messagebox.showinfo("Balanced", f"{name}, thanks for sharing. Remember, balance is key.\n\nAffirmation: {aff}")
    else:
        aff = random.choice(aff_list)
        messagebox.showinfo("Great!", f"Awesome mood today, {name}! Keep that spirit up! 🌟\n\nAffirmation: {aff}")

    # follow up for low mood
    if mood <= 2:
        choice = messagebox.askquestion("More help?", "Would you like coping strategies? (No = affirmations)")
        if choice == "yes":
            messagebox.showinfo("Coping", random.choice(calming_tips))
        else:
            messagebox.showinfo("Affirmation", random.choice(affirmations_motivational))
    else:
        messagebox.showinfo("Take care", "Keep shining and take care!")

    messagebox.showinfo("Session end", f"Thank you for chatting, {'' if anon else name}.\nYour mood history this session: {mood_history}")

# Build simple main window
root = tk.Tk()
root.title("Numa — GUI")

frame = tk.Frame(root, padx=12, pady=12)
frame.pack()

tk.Label(frame, text="Numa — your personalized mental health assistant").grid(row=0, column=0, columnspan=2, pady=(0,10))

tk.Label(frame, text="Name:").grid(row=1, column=0, sticky="e")
name_var = tk.StringVar()
tk.Entry(frame, textvariable=name_var).grid(row=1, column=1, sticky="w")

anon_var = tk.IntVar(value=0)
tk.Checkbutton(frame, text="Use anonymously", variable=anon_var).grid(row=2, column=0, columnspan=2, sticky="w")

tk.Label(frame, text="Affirmation style:").grid(row=3, column=0, sticky="e")
style_var = tk.IntVar(value=1)
tk.Radiobutton(frame, text="Motivational", variable=style_var, value=1).grid(row=3, column=1, sticky="w")
tk.Radiobutton(frame, text="Soothing", variable=style_var, value=2).grid(row=4, column=1, sticky="w")

reminder_var = tk.IntVar(value=0)
tk.Checkbutton(frame, text="Show reminder at start", variable=reminder_var).grid(row=5, column=0, columnspan=2, sticky="w")

tk.Button(frame, text="Start Session", command=start_session, width=20).grid(row=6, column=0, columnspan=2, pady=(10,0))

root.mainloop()
