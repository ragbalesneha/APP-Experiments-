from abc import ABC, abstractmethod


class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount: float) -> None:
        """Abstract method to execute payment logic."""
        pass



class CreditCardPayment(PaymentStrategy):

    def __init__(self, card_number: str, holder_name: str):
        self.card_number = card_number
        self.holder_name = holder_name

    def pay(self, amount: float) -> None:
        masked_card = f"****-****-****-{self.card_number[-4:]}"
        print(
            f"Processing ₹{amount:.2f} via Credit Card ({masked_card}) - Holder: {self.holder_name}."
        )



class PayPalPayment(PaymentStrategy):

    def __init__(self, email: str):
        self.email = email

    def pay(self, amount: float) -> None:
        print(f"Processing ₹{amount:.2f} via PayPal account ({self.email}).")



class UPIPayment(PaymentStrategy):

    def __init__(self, upi_id: str):
        self.upi_id = upi_id

    def pay(self, amount: float) -> None:
        print(f"Processing ₹{amount:.2f} via UPI ID ({self.upi_id}).")



class PaymentContext:

    def __init__(self, strategy: PaymentStrategy = None):
        """Initialize context with an optional payment strategy."""
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy) -> None:
        """Dynamically set or change the payment strategy at runtime."""
        self._strategy = strategy

    def execute_payment(self, amount: float) -> None:
        """Executes the payment using the current strategy."""
        if self._strategy is None:
            raise ValueError(
                "No payment strategy configured. Please set a strategy before proceeding."
            )
        self._strategy.pay(amount)


if __name__ == "__main__":
    print("--- Configurable Payment Processing System ---\n")

    
    checkout = PaymentContext()

    # Scenario 1: User chooses Credit Card
    print("Scenario 1: Paying with Credit Card")
    credit_card = CreditCardPayment(
        card_number="4532112233445566", holder_name="Sneha Ragbale"
    )
    checkout.set_strategy(credit_card)
    checkout.execute_payment(1250.50)

    print("\n" + "-" * 45 + "\n")

    # Scenario 2: User switches strategy to PayPal
    print("Scenario 2: Changing strategy to PayPal")
    paypal = PayPalPayment(email="user@example.com")
    checkout.set_strategy(paypal)
    checkout.execute_payment(450.00)

    print("\n" + "-" * 45 + "\n")

    # Scenario 3: User switches strategy to UPI
    print("Scenario 3: Changing strategy to UPI")
    upi = UPIPayment(upi_id="sneha@okaxis")
    checkout.set_strategy(upi)
    checkout.execute_payment(899.00)