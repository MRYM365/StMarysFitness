import unittest
from unittest.mock import MagicMock
from gui.main_gui import FitnessManagementApp
import tkinter as tk

class TestGUINavigation(unittest.TestCase):
    def setUp(self):
        # Create a root window for the tests
        self.root = tk.Tk()
        self.app = FitnessManagementApp(self.root)

    def tearDown(self):
        # Destroy the root window after each test
        self.root.destroy()

    def test_navigation_to_manage_members(self):
        """Test if clicking 'Manage Members' updates the content area."""
        # Simulate clicking the "Manage Members" button
        self.app.show_manage_members()

        # Check if the content area has the correct title
        content_widgets = [widget for widget in self.app.content_frame.winfo_children() if isinstance(widget, tk.Label)]
        self.assertTrue(any("Manage Members" in widget.cget("text") for widget in content_widgets))

    def test_navigation_to_manage_gyms(self):
        """Test if clicking 'Manage Gym Locations' updates the content area."""
        # Simulate clicking the "Manage Gyms" button
        self.app.show_manage_gyms()

        # Check if the content area has the correct title
        content_widgets = [widget for widget in self.app.content_frame.winfo_children() if isinstance(widget, tk.Label)]
        self.assertTrue(any("Manage Gym Locations" in widget.cget("text") for widget in content_widgets))

    def test_navigation_to_dashboard(self):
        """Test if clicking 'View Dashboard' updates the content area."""
        # Simulate clicking the "Staff Management Dashboard" button
        self.app.show_staff_dashboard()

        # Check if the content area has the correct title
        content_widgets = [widget for widget in self.app.content_frame.winfo_children() if isinstance(widget, tk.Label)]
        self.assertTrue(any("Staff Management Dashboard" in widget.cget("text") for widget in content_widgets))


if __name__ == "__main__":
    unittest.main()
