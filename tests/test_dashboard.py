import unittest
from unittest.mock import patch
from controllers.dashboard_controller import DashboardController


class TestDashboard(unittest.TestCase):
    @patch("views.dashboard_view.DashboardView.display_membership_metrics")
    def test_generate_membership_metrics(self, mock_display):
        mock_members = [
            {"membership_type": "Regular"},
            {"membership_type": "Premium"},
            {"membership_type": "Trial"},
            {"membership_type": "Premium"},
        ]
        controller = DashboardController(mock_members, [], {}, [])
        controller.generate_membership_metrics()

        # Capture the metrics passed to the view
        metrics = mock_display.call_args[0][0]  # Extract the first argument passed to the mocked method

        self.assertEqual(metrics["total_members"], 4)
        self.assertEqual(metrics["premium_members"], 2)


if __name__ == "__main__":
    unittest.main()
