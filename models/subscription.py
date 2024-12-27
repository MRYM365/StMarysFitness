class Subscription:
    def __init__(self, subscription_id, member, plan, fee, discount=0):
        self.subscription_id = subscription_id
        self.member = member
        self.plan = plan  # Monthly, Quarterly, Annual
        self.fee = fee
        self.discount = discount
        self.status = "inactive"  # active, expired

    def calculate_final_fee(self):
        return self.fee - (self.fee * self.discount / 100)

    def activate_subscription(self):
        self.status = "active"

    def expire_subscription(self):
        self.status = "expired"
