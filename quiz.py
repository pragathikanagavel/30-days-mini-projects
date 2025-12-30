import csv
import random
import os
from datetime import date

SCORE_FILE = "scores.csv"

# Create score file if not exists
if not os.path.exists(SCORE_FILE):
    with open(SCORE_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Date", "Topic", "Score"])

# Question bank
QUIZ = {
    "python": [
        ("Which keyword is used to define a function?",
         ["A. func", "B. define", "C. def", "D. function"], "C"),

        ("Which data type is immutable?",
         ["A. list", "B. dict", "C. set", "D. tuple"], "D"),

        ("What is the output of len('Python')?",
         ["A. 5", "B. 6", "C. 7", "D. Error"], "B"),
    ],

    "aptitude": [
        ("5 + 3 * 2 = ?",
         ["A. 16", "B. 11", "C. 10", "D. 13"], "B"),

        ("Average of 2,4,6?",
         ["A. 3", "B. 4", "C. 5", "D. 6"], "B"),

        ("10% of 200?",
         ["A. 10", "B. 15", "C. 20", "D. 25"], "C"),
    ]
}


def take_quiz(name):
    print("\nAvailable Topics:")
    for topic in QUIZ:
        print("-", topic)

    topic = input("Choose topic: ").lower()
    if topic not in QUIZ:
        print("Invalid topic!")
        return

    questions = random.sample(QUIZ[topic], 3)
    score = 0
    wrong_questions = []

    for q, options, answer in questions:
        print("\n", q)
        for opt in options:
            print(opt)

        user_ans = input("Your answer (A/B/C/D): ").upper()

        if user_ans == answer:
            score += 1
            print("Correct ✔")
        else:
            score -= 0.25
            wrong_questions.append((q, options, answer))
            print("Wrong ✘ | Correct:", answer)

    percent = (score / len(questions)) * 100

    print("\nFinal Score:", round(score, 2))
    print("Percentage:", round(percent, 2), "%")

    if percent >= 60:
        print("Result: PASS ✅")
    else:
        print("Result: FAIL ❌")

    # Save score
    with open(SCORE_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, date.today(), topic, round(score, 2)])

    # Retry wrong questions
    if wrong_questions:
        retry = input("\nRetry wrong questions? (y/n): ").lower()
        if retry == "y":
            retry_wrong(wrong_questions)


def retry_wrong(wrong_questions):
    print("\nRetrying wrong questions...")
    for q, options, answer in wrong_questions:
        print("\n", q)
        for opt in options:
            print(opt)

        user_ans = input("Your answer: ").upper()
        if user_ans == answer:
            print("Correct now ✔")
        else:
            print("Still wrong ✘ | Correct:", answer)


def leaderboard():
    print("\n--- Leaderboard ---")
    scores = []

    with open(SCORE_FILE, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            scores.append(row)

    scores.sort(key=lambda x: float(x[3]), reverse=True)

    for i, row in enumerate(scores[:3], start=1):
        print(f"{i}. {row[0]} - {row[3]}")


def main():
    name = input("Enter your name: ")

    while True:
        print("\n--- Smart Quiz App ---")
        print("1. Take Quiz")
        print("2. View Leaderboard")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            take_quiz(name)
        elif choice == "2":
            leaderboard()
        elif choice == "3":
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
