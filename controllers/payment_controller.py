from models.payment import Payment
from views.payment_view import PaymentView

class PaymentController:
    def __init__(self):
        self.payments = {}

    def process_payment(self, payment_id, subscription, amount, payment_method):
        payment = Payment(payment_id, subscription, amount, "2024-01-15", payment_method)
        self.payments[payment_id] = payment
        print("Payment processed successfully!")

    def display_payment(self, payment_id):
        if payment_id in self.payments:
            PaymentView.display_payment_details(self.payments[payment_id])
        else:
            print("Payment not found.")
