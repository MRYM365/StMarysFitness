import unittest
from models.payment import Payment

class TestPayment(unittest.TestCase):
    def test_create_payment(self):
        """Test creating a payment record."""
        payment = Payment("P001", "Monthly", 100.0, "2024-01-01", "Credit Card")
        self.assertEqual(payment.payment_id, "P001")
        self.assertEqual(payment.subscription, "Monthly")
        self.assertEqual(payment.amount, 100.0)
        self.assertEqual(payment.payment_date, "2024-01-01")
        self.assertEqual(payment.payment_method, "Credit Card")

    def test_payment_amount(self):
        """Test the payment amount."""
        payment = Payment("P002", "Annual", 1200.0, "2024-01-01", "Bank Transfer")
        self.assertEqual(payment.amount, 1200.0)

    def test_subscription_type(self):
        """Test the subscription type for the payment."""
        payment = Payment("P003", "Quarterly", 300.0, "2024-01-01", "Cash")
        self.assertEqual(payment.subscription, "Quarterly")

if __name__ == "__main__":
    unittest.main()
