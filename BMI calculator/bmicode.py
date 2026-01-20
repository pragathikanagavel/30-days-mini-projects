

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def health_status(bmi):
    if bmi < 18.5:
        return "Underweight", "Increase calorie intake with nutritious food."
    elif 18.5 <= bmi < 25:
        return "Normal", "Maintain a balanced diet and regular exercise."
    elif 25 <= bmi < 30:
        return "Overweight", "Reduce sugar intake and do regular physical activity."
    else:
        return "Obese", "Consult a healthcare professional and follow a strict fitness plan."

def main():
    print("=== BMI & Health Risk Calculator ===")

    try:
        weight = float(input("Enter your weight (in kg): "))
        height = float(input("Enter your height (in meters): "))

        if weight <= 0 or height <= 0:
            print("Weight and height must be positive values.")
            return

        bmi = calculate_bmi(weight, height)
        status, advice = health_status(bmi)

        print("\n--- Result ---")
        print(f"BMI Value      : {bmi}")
        print(f"Health Status  : {status}")
        print(f"Advice         : {advice}")

    except ValueError:
        print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    main()
