import unittest
from controllers.dashboard_controller import DashboardController

class TestDashboard(unittest.TestCase):
    def test_generate_membership_metrics(self):
        mock_members = [
            {"membership_type": "Regular"},
            {"membership_type": "Premium"},
            {"membership_type": "Trial"},
            {"membership_type": "Premium"},
        ]
        controller = DashboardController(mock_members, [], {}, [])
        metrics = controller.generate_membership_metrics()
        self.assertEqual(metrics["total_members"], 4)
        self.assertEqual(metrics["premium_members"], 2)

if __name__ == "__main__":
    unittest.main()
