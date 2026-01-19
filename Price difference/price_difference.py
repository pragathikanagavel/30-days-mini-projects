print("Day 27 - Farmer to Consumer Price Comparison Tool")

market_prices = {
    "tomato": 40,
    "onion": 35,
    "potato": 30,
    "brinjal": 45,
    "carrot": 50,
    "cabbage": 25,
    "cauliflower": 30,
    "beans": 60,
    "peas": 70,
    "capsicum": 55,
    "chilli": 90,
    "ginger": 120,
    "garlic": 150,
    "cucumber": 30,
    "pumpkin": 20,
    "radish": 28,
    "spinach": 20,
    "banana": 50,
    "apple": 180,
    "orange": 80,
    "grapes": 90,
    "mango": 120
}

crop = input("Enter crop name: ").lower()
farmer_price = float(input("Enter farmer price per kg (₹): "))

if crop in market_prices:
    market_price = market_prices[crop]
    difference = market_price - farmer_price
    percentage = (difference / farmer_price) * 100

    print("\n--- Price Analysis ---")
    print(f"Crop Name: {crop.capitalize()}")
    print(f"Farmer Price: ₹{farmer_price}/kg")
    print(f"Market Price (Current): ₹{market_price}/kg")
    print(f"Price Difference: ₹{difference:.2f}/kg")
    print(f"Increase Percentage: {percentage:.2f}%")

    if difference > 0:
        print("Insight: Farmers are underpaid. Middlemen gain higher profit.")
    elif difference == 0:
        print("Insight: Fair pricing observed.")
    else:
        print("Insight: Farmer price is higher than market price.")
else:
    print("Crop not found in market database.")
    print("Available crops:", ", ".join(market_prices.keys()))
