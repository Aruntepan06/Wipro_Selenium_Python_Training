# LAB 8: Real-Time Payment System (Polymorphism)

class Payment:
    def pay(self, amount):
        print(f"Paying {amount} using base Payment")


class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")


class UPI(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")


class NetBanking(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using NetBanking")


def process_payment(payment_obj, amount):
    payment_obj.pay(amount)


process_payment(CreditCard(), 1000)
process_payment(UPI(), 500)
process_payment(NetBanking(), 2500)
