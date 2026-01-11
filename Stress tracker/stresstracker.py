from datetime import date

print(" Welcome to the Stress Level Checker \n")

# 1. Personalization
name = input("Enter your name: ")

print("\nPlease answer the following questions")
print("Scale: 1 = Never, 5 = Always\n")

# Questions with categories
questions = {
    "Sleep": [
        "Do you have trouble sleeping?",
    ],
    "Work/Study": [
        "Do you feel stressed about work or studies?",
    ],
    "Emotional": [
        "Do you feel irritated or moody often?",
    ],
    "Physical": [
        "Do you feel physically tired most of the time?",
        "Do you feel lack of relaxation or free time?"
    ]
}

total_score = 0
category_scores = {}

# 2. Input Validation + 3. Category-based analysis
for category, qs in questions.items():
    category_scores[category] = 0
    for q in qs:
        while True:
            try:
                ans = int(input(q + " "))
                if 1 <= ans <= 5:
                    category_scores[category] += ans
                    total_score += ans
                    break
                else:
                    print("❗ Please enter a number between 1 and 5.")
            except ValueError:
                print("❗ Invalid input. Enter numbers only.")

# Stress Level Calculation
print("\n Stress Analysis Result")
print(f"Name: {name}")
print(f"Total Stress Score: {total_score}")

if total_score <= 8:
    stress_level = "LOW"
elif total_score <= 15:
    stress_level = "MODERATE"
else:
    stress_level = "HIGH "

print(f"Stress Level: {stress_level}")

# 4. Activity Recommendation System
print("\n Recommended Activities:")
if "HIGH" in stress_level:
    print("- Try deep breathing exercises")
    print("- Take a short walk")
    print("- Talk to someone you trust")
elif "MODERATE" in stress_level:
    print("- Take short breaks while working")
    print("- Listen to calming music")
    print("- Maintain a healthy routine")
else:
    print("- Keep up your positive habits")
    print("- Stay consistent with self-care")

# Category Breakdown
print("\n Category Breakdown:")
for cat, score in category_scores.items():
    print(f"{cat}: {score}")

# 5. Stress History Logging
today = date.today()
with open("stress_log.txt", "a") as file:
    file.write(f"{today} | {name} | Score: {total_score} | Level: {stress_level}\n")

print("\n Your stress data has been saved successfully.")
print(" Reminder: This tool is for self-reflection, not medical advice.")
