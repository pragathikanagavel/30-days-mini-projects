from datetime import date

print("🧠 PERSONAL WARNING SYSTEM – Burnout Checker")
print("-" * 45)

try:
    mood = int(input("Rate your mood (1 = Very Low, 5 = Very Good): "))
    sleep = float(input("How many hours did you sleep last night? "))
    stress = int(input("Rate your stress level (1 = Low, 5 = High): "))

    burnout_score = 0

    # Mood logic
    if mood <= 2:
        burnout_score += 3
    elif mood == 3:
        burnout_score += 1

    # Sleep logic
    if sleep < 5:
        burnout_score += 3
    elif sleep < 7:
        burnout_score += 1

    # Stress logic
    if stress >= 4:
        burnout_score += 3
    elif stress == 3:
        burnout_score += 1

    # Result analysis
    if burnout_score <= 2:
        status = "🟢 SAFE"
        advice = "You're doing well. Maintain balance and hydration."
    elif burnout_score <= 5:
        status = "🟡 ALERT"
        advice = "Slow down. Take breaks and get proper sleep."
    else:
        status = "🔴 CRITICAL"
        advice = "High burnout risk! Rest immediately and reduce workload."

    today = date.today()

    print("\n📊 RESULT")
    print("-" * 20)
    print(f"Date: {today}")
    print(f"Burnout Status: {status}")
    print(f"Advice: {advice}")

    # Save to file
    with open("burnout_log.txt", "a", encoding="utf-8") as file:
        file.write(f"{today} | Mood:{mood} | Sleep:{sleep} | Stress:{stress} | {status}\n")

    print("\n✅ Data saved to burnout_log.txt")

except ValueError:
    print("❌ Please enter valid numeric inputs.")
