import random

# Session mood history
mood_history = []

# Affirmations styles
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

def get_user_input(prompt):
    """Simple input prompt with strip."""
    response = input(prompt + " ")
    return response.strip()

def record_mood():
    """Capture user's mood rating 1 to 5, validate input."""
    while True:
        try:
            mood = int(get_user_input("On a scale of 1 (worst) to 5 (best), how are you feeling right now?"))
            if 1 <= mood <= 5:
                mood_history.append(mood)
                return mood
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input, please enter a number.")

def choose_option(prompt, options):
    """Prompt user to choose from available options."""
    print(prompt)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    while True:
        choice = get_user_input("Enter the number of your choice:")
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice)
        else:
            print("Invalid choice, please select a valid number.")

def personalized_response(name, mood, affirmation_style):
    """Respond based on mood and chosen affirmation style."""
    if affirmation_style == 1:
        affirmations = affirmations_motivational
    else:
        affirmations = affirmations_soothing
    
    if mood <= 2:
        print(f"\n{name}, it seems you've had a tough day. Here's something to help you:")
        print(random.choice(calming_tips))
    elif mood == 3:
        print(f"\n{name}, thanks for sharing. Remember, balance is key, and you're doing great.")
        print(random.choice(affirmations))
    else:
        print(f"\nAwesome mood today, {name}! Keep that spirit up! 🌟")
        print(random.choice(affirmations))

def detect_urgent_keywords(text):
    """Warn user if serious keywords detected."""
    urgent_keywords = ["hurt", "suicide", "depressed", "sad", "lonely", "anxious"]
    lower_text = text.lower()
    if any(word in lower_text for word in urgent_keywords):
        print("\nIf you are feeling overwhelmed, consider talking to a trusted person or a professional helpline.")

def ask_follow_up(mood):
    """Ask user if they want tips or affirmations; respond accordingly."""
    if mood <= 2:
        coping = get_user_input("Would you like some coping strategies or motivational affirmations? (type 'coping' or 'affirmation')")
        if coping.lower() == "coping":
            print(random.choice(calming_tips))
        elif coping.lower() == "affirmation":
            print(random.choice(affirmations_motivational))
        else:
            print("Thanks for chatting. Remember, small steps make a difference!")
    else:
        print("Keep shining and take care!")

def user_customizations():
    """Allow user to customize reminders, affirmation style, and anonymity."""
    anon_mode = choose_option("Would you like to use Numa anonymously?", ["No (use my name)", "Yes (anonymous mode)"]) == 2
    
    affirmation_style = choose_option(
        "Choose your preferred style of affirmations:",
        ["Motivational", "Soothing"]
    )
    
    reminder_opt = choose_option(
        "Would you like to receive a daily reminder from Numa?",
        ["No", "Yes (You will get a motivational quote when you start)"]
    )
    
    return anon_mode, affirmation_style, reminder_opt

def main():
    print("Welcome to Numa - your personalized mental health assistant.\n")
    
    # Get user customization preferences
    anon_mode, affirmation_style, reminder_opt = user_customizations()
    
    # Handle anonymous mode
    if anon_mode:
        user_name = "Friend"
    else:
        user_name = get_user_input("Great! What’s your name?")
    
    print(f"\nHi {user_name}! Let's talk about your day.")
    
    # Start session with optional reminder
    if reminder_opt == 2:
        if affirmation_style == 1:
            print(random.choice(affirmations_motivational))
        else:
            print(random.choice(affirmations_soothing))
    
    # User mood and chat flow
    mood = record_mood()
    highlight = get_user_input("What’s one good thing that happened today?")
    detect_urgent_keywords(highlight)
    worry = get_user_input("Is there something bothering you that you'd like to share?")
    detect_urgent_keywords(worry)
    
    personalized_response(user_name, mood, affirmation_style)
    ask_follow_up(mood)
    
    print(f"\nThank you for chatting with Numa, {user_name if not anon_mode else ''}. Remember, you are not alone. Take care! 💙")
    
    print(f"\nYour mood history this session: {mood_history}")

if __name__ == "__main__":
    main()
