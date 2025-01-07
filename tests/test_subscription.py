import unittest
from models.subscription import Subscription

class TestSubscription(unittest.TestCase):
    def test_create_subscription(self):
        """Test creating a subscription."""
        subscription = Subscription("S001", "Member1", "Monthly", 100.0, 10)
        self.assertEqual(subscription.subscription_id, "S001")
        self.assertEqual(subscription.member, "Member1")
        self.assertEqual(subscription.plan, "Monthly")
        self.assertEqual(subscription.fee, 100.0)
        self.assertEqual(subscription.discount, 10)
        self.assertEqual(subscription.status, "inactive")

    def test_calculate_final_fee(self):
        """Test calculating the final fee with discount."""
        subscription = Subscription("S001", "Member1", "Monthly", 100.0, 10)
        final_fee = subscription.calculate_final_fee()
        self.assertEqual(final_fee, 90.0)  # 10% discount applied

    def test_activate_subscription(self):
        """Test activating a subscription."""
        subscription = Subscription("S001", "Member1", "Monthly", 100.0, 10)
        subscription.activate_subscription()
        self.assertEqual(subscription.status, "active")

    def test_expire_subscription(self):
        """Test expiring a subscription."""
        subscription = Subscription("S001", "Member1", "Monthly", 100.0, 10)
        subscription.expire_subscription()
        self.assertEqual(subscription.status, "expired")

if __name__ == "__main__":
    unittest.main()
