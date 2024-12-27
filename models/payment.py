class Payment:
    def __init__(self, payment_id, subscription, amount, payment_date, payment_method):
        self.payment_id = payment_id
        self.subscription = subscription
        self.amount = amount
        self.payment_date = payment_date
        self.payment_method = payment_method
