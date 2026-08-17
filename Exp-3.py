# -----------------------------
# Strategy Pattern Example
# -----------------------------

# Parent Class (Base Strategy)
class PaymentStrategy:
    def pay(self, amount):
        pass


# Credit Card Strategy
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


# PayPal Strategy
class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal")


# Context Class
class PaymentContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def pay(self, amount):
        self.strategy.pay(amount)


# -----------------------------
# Main Program
# -----------------------------

amount = float(input("Enter payment amount: ₹"))

print("\nChoose Payment Method:")
print("1. Credit Card")
print("2. PayPal")

choice = int(input("Enter your choice: "))

if choice == 1:
    strategy = CreditCardPayment()
elif choice == 2:
    strategy = PayPalPayment()
else:
    print("Invalid choice!")
    exit()

payment = PaymentContext(strategy)

payment.pay(amount)