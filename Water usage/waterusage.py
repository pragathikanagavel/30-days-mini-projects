def water_usage_estimator():
    people = int(input("Enter number of people in the house: "))
    buckets = int(input("Buckets used per person per day: "))
    washing = int(input("Washing machine uses per week: "))
    bath_type = input("Bath type (bucket/shower): ").lower()

    bucket_water = buckets * 15 * people
    washing_water = (washing * 70) / 7

    if bath_type == "shower":
        bath_water = 50 * people
    else:
        bath_water = 0

    total_daily_usage = bucket_water + washing_water + bath_water

    print("\n🚰 Estimated Water Usage")
    print(f"Average Daily Usage: {total_daily_usage:.2f} liters")

    if total_daily_usage > 500:
        print("⚠️ High usage detected. Consider conservation.")
    else:
        print("✅ Usage is within normal range.")

water_usage_estimator()
