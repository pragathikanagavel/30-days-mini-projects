import random

def mood_quote_generator():
    quotes = {
        "happy": [
            "Happiness is a journey, not a destination.",
            "Smile, it makes you attractive.",
            "Enjoy the little things in life."
        ],
        "sad": [
            "This too shall pass.",
            "Every storm runs out of rain.",
            "Tough times never last, but tough people do."
        ],
        "stressed": [
            "Breathe. You are doing better than you think.",
            "Slow down, you're doing fine.",
            "Take one step at a time."
        ],
        "motivated": [
            "Push yourself, because no one else will.",
            "Success starts with self-belief.",
            "Dream it. Wish it. Do it."
        ]
    }

    print("Choose your mood: Happy / Sad / Stressed / Motivated")
    mood = input("Enter your mood: ").lower()

    if mood in quotes:
        print("\n✨ Quote for you:")
        print(random.choice(quotes[mood]))
    else:
        print("\n❌ Mood not found. Please choose a valid mood.")

mood_quote_generator()
