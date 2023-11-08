# Task. Refactor class to comply with SOLID principles.

class Order:
    items = []
    quantities = []
    prices = []
    status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total = total + self.quantities[i] * self.prices[i]
        return total


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 50)



from abc import abstractmethod, ABC

class PaymentProcessorSMS(ABC):

    def set_status(self, order):
        order.status = "paid"

    @abstractmethod
    def auth_sms(self, code):
        pass

    @abstractmethod
    def pay(self, order):
        pass

class PaymentProcessor(ABC):

    def set_status(self, order):
        order.status = "paid"

    @abstractmethod
    def pay(self, order):
        pass

class DebitPaymentProcessor(PaymentProcessorSMS):
    def __init__(self, security_code: int) -> None:
        super().__init__()
        self.security_code = security_code
        self.verified = False

    def auth_sms(self, code):
        print(f"Verifying the code{code}.")
        self.verified = True

    def pay(self, order):
        if not self.verified:
            raise Exception("Payment not authorized.")
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        self.set_status(order)

class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code: int) -> None:
        super().__init__()
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        self.set_status(order)

class PayPalPaymentProcessor(PaymentProcessor):

    def __init__(self, email: str) -> None:
        super().__init__()
        self.email = email

    def pay(self, order):
        print("Processing PayPal payment type")
        print(f"Verifying e-mail: {self.email}")
        self.set_status(order)

payment_processor = DebitPaymentProcessor(1234)
# payment_processor.auth_sms(123)
payment_processor.pay(order)