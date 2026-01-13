import random

fortunes = [
    "You will debug successfully today!",
    "An opcode remembered is a mark of wisdom.",
    "Patience in coding brings clarity.",
    "Your exam prep will pay off soon!",
    "A small bug fixed is a big victory."
]

print("🥠 Welcome to the Digital Fortune Cookie!")
print("Press Enter to crack a cookie, or type 'q' to quit.\n")

last_fortune = None   # To track previous fortune
count = 0             # Fortune tracker

while True:
    choice = input("👉 Crack a cookie (Enter) or quit (q): ").lower()
    
    if choice == 'q':
        print(f"\n🍪 You cracked {count} cookies today. Goodbye!")
        break
    
    # Pick a fortune that is not the same as last time
    fortune = random.choice(fortunes)
    while fortune == last_fortune:
        fortune = random.choice(fortunes)
    
    print("\n🥠 Your Fortune Cookie says:")
    print(fortune)
    
    # Update trackers
    last_fortune = fortune
    count += 1
    print("-" * 40)  # Divider for clarity