appliances = {
    "Fan": 0.075,
    "Light": 0.02,
    "AC": 1.5,
    "Refrigerator": 1.0,
    "Washing Machine": 0.5
}

total_units = 0

print("🔌 Smart Energy Consumption Simulator\n")

for appliance, power in appliances.items():
    hours = float(input(f"Enter daily usage hours for {appliance}: "))
    units = power * hours
    total_units += units

monthly_units = total_units * 30
bill = monthly_units * 6  # Rs.6 per unit (approx)

print("\n📊 Monthly Energy Report")
print(f"Total Units Consumed: {monthly_units:.2f} kWh")
print(f"Estimated Electricity Bill: ₹{bill:.2f}")

if monthly_units > 300:
    print("⚠️ High consumption detected. Consider reducing AC usage.")
else:
    print("✅ Energy usage is under control.")
