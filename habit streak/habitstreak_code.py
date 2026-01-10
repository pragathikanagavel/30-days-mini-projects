print("🌱 Daily Habit Tracker – Premium Version 🌱")

# Habit selection
print("\nChoose a habit:")
print("1. Coding")
print("2. Drinking Water")
print("3. Exercise")

choice = input("Enter choice (1/2/3): ")

if choice == "1":
    habit = "Coding"
elif choice == "2":
    habit = "Drinking Water"
elif choice == "3":
    habit = "Exercise"
else:
    habit = None

if habit is None:
    print("❌ Invalid choice")
else:
    # Mood input
    print("\nHow do you feel today?")
    print("1. Happy 😊")
    print("2. Neutral 😐")
    print("3. Tired 😞")
    mood = input("Enter mood (1/2/3): ")

    # Completion status
    status = input("\nDid you complete this habit today? (yes/no): ").lower()

    # Time spent
    time_spent = int(input("How many minutes did you spend? "))

    # Simple streak (assume previous streak = 3 for demo)
    streak = 3

    if status == "yes":
        streak += 1
        print(f"\n✅ Well done! You completed {habit}.")
        print(f"🔥 Current Streak: {streak} days")
        print(f"⏱️ Time Spent: {time_spent} minutes")

        # Reflection
        reflection = input("✍️ What went well today? ")
        print("Reflection saved. Keep going!")

    else:
        streak = 0
        print(f"\n🤍 It's okay. Missing one day doesn’t break your journey.")
        print(f"👉 Try just 5 minutes of {habit} tomorrow.")
        print("Consistency > Perfection")

    # Mood-based message
    if mood == "1":
        print(" Great energy today!")
    elif mood == "2":
        print(" You still showed up. That matters.")
    else:
        print(" Even trying on hard days is progress.")
