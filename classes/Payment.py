class Payment:
    def pay(self,amount:float):
        raise NotImplementedError


class CreditCardPayment (Payment):
    def pay(self,amount:float):
        print(f"payment for using credit card:{amount}")


class PayPalPayment (Payment):
    def pay(self,amount:float):
         print(f"payment for using pal card:{amount}")


class CryptoPayment(Payment):
    def pay(self, amount: float):
        print(f"Paid {amount} in cryptocurrency.")