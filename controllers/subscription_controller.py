from models.subscription import Subscription
from views.payment_view import PaymentView

class SubscriptionController:
    def __init__(self):
        self.subscriptions = {}

    def create_subscription(self, subscription_id, member, plan, fee, discount):
        subscription = Subscription(subscription_id, member, plan, fee, discount)
        self.subscriptions[subscription_id] = subscription
        subscription.activate_subscription()
        print("Subscription created and activated!")

    def expire_subscription(self, subscription_id):
        if subscription_id in self.subscriptions:
            self.subscriptions[subscription_id].expire_subscription()
            print("Subscription expired.")
        else:
            print("Subscription not found.")

    def display_subscription(self, subscription_id):
        if subscription_id in self.subscriptions:
            PaymentView.display_subscription_details(self.subscriptions[subscription_id])
        else:
            print("Subscription not found.")
