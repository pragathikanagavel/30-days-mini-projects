# Payment Method Simulator
# Demonstrates Inheritance and Polymorphism in Python


# Parent Class
class Payment:
    def __init__(self, amount):
        self.amount = amount

    def pay(self):
        print("Processing payment...")


# Child Class - UPI
class UPIPayment(Payment):
    def pay(self):
        print(f"✅ Paid ₹{self.amount} using UPI")


# Child Class - Card
class CardPayment(Payment):
    def pay(self):
        print(f"💳 Paid ₹{self.amount} using Debit/Credit Card")


# Child Class - Cash
class CashPayment(Payment):
    def pay(self):
        print(f"💵 Paid ₹{self.amount} using Cash")


# Polymorphism Function
def make_payment(payment_method):
    payment_method.pay()


# Main Program
def main():
    try:
        amount = int(input("Enter payment amount: ₹"))

        print("\nChoose payment method:")
        print("1. UPI")
        print("2. Card")
        print("3. Cash")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            payment = UPIPayment(amount)
        elif choice == "2":
            payment = CardPayment(amount)
        elif choice == "3":
            payment = CashPayment(amount)
        else:
            print("❌ Invalid choice")
            return

        make_payment(payment)

    except ValueError:
        print("❌ Please enter a valid number for amount")


# Run Program
main()
