# Simple Memory Museum

rooms = {
    "entry": {
        "text": "You are at the museum entrance.",
        "options": ["discipline", "failure", "exit"]
    },
    "discipline": {
        "text": "This room talks about consistency and habits.",
        "options": ["growth", "entry"]
    },
    "failure": {
        "text": "This room stores lessons from mistakes.",
        "options": ["discipline", "exit"]
    },
    "growth": {
        "text": "This room represents personal growth.",
        "options": ["entry", "exit"]
    }
}

current_room = "entry"

while True:
    print("\n----------------------")
    print(rooms[current_room]["text"])
    print("You can go to:")

    for opt in rooms[current_room]["options"]:
        print("-", opt)

    choice = input("Enter your choice: ").lower()

    if choice in rooms[current_room]["options"]:
        if choice == "exit":
            print("\nYou leave the museum. Session ended.")
            break
        current_room = choice
    else:
        print("Invalid choice. Try again.")
