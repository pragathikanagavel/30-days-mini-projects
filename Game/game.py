import random

def play_game():
    print("\n🎮 Number Guessing Game")
    print("Choose Difficulty Level:")
    print("1. Easy (1–50, 10 attempts)")
    print("2. Medium (1–100, 7 attempts)")
    print("3. Hard (1–200, 5 attempts)")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        max_num, attempts = 50, 10
    elif choice == "2":
        max_num, attempts = 100, 7
    elif choice == "3":
        max_num, attempts = 200, 5
    else:
        print("Invalid choice! Defaulting to Medium.")
        max_num, attempts = 100, 7

    number = random.randint(1, max_num)
    guesses = []

    print(f"\nGuess a number between 1 and {max_num}")

    while attempts > 0:
        guess = int(input("Enter your guess: "))
        guesses.append(guess)

        if guess == number:
            print("🎉 You guessed it right!")
            print("Score:", attempts * 10)
            break
        elif guess > number:
            print("Too high!")
        else:
            print("Too low!")

        attempts -= 11
        print("Attempts left:", attempts)

    if attempts == 0:
        print("\n😢 Game Over!")
        print("The number was:", number)

    print("Your guesses:", guesses)

def main():
    while True:
        play_game()
        again = input("\nDo you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing! 👋")
            break

main()
