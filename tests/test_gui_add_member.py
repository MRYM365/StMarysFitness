import unittest
from unittest.mock import patch
from tkinter import messagebox
from gui.main_gui import FitnessManagementApp
import tkinter as tk


class TestAddMemberForm(unittest.TestCase):
    def setUp(self):
        # Create a root window for testing
        self.root = tk.Tk()
        self.app = FitnessManagementApp(self.root)

    def tearDown(self):
        # Destroy the root window after testing
        self.root.destroy()

    @patch("tkinter.messagebox.showerror")
    def test_missing_fields_validation(self, mock_showerror):
        """Test validation for missing fields in Add Member form."""
        # Open the Add Member form
        self.app.show_add_member_form()

        # Simulate empty input fields and click Add Member button
        self.app.add_member("", "", "", "", "", "")

        # Check if an error message is displayed
        mock_showerror.assert_called_with("Input Error", "All fields except Medical Conditions are required!")

    @patch("tkinter.messagebox.showerror")
    def test_invalid_age_validation(self, mock_showerror):
        """Test validation for invalid age input."""
        # Open the Add Member form
        self.app.show_add_member_form()

        # Simulate invalid age input and click Add Member button
        self.app.add_member("John Doe", "Regular", "-1", "175", "70", "")

        # Check if an error message is displayed
        mock_showerror.assert_called_with("Input Error", "Age must be a positive number!")

    @patch("tkinter.messagebox.showinfo")
    def test_successful_member_addition(self, mock_showinfo):
        """Test successful addition of a member."""
        # Open the Add Member form
        self.app.show_add_member_form()

        # Simulate valid inputs and click Add Member button
        self.app.add_member("John Doe", "Regular", "30", "175", "70", "None")

        # Check if the success message is displayed
        mock_showinfo.assert_called_with("Success", "Member 'John Doe' added successfully!")

        # Check if the member is added to the members list
        added_member = self.app.members[-1]  # Get the last added member
        self.assertEqual(added_member["name"], "John Doe")
        self.assertEqual(added_member["membership_type"], "Regular")
        self.assertEqual(added_member["age"], 30)
        self.assertEqual(added_member["height"], 175)
        self.assertEqual(added_member["weight"], 70)
        self.assertEqual(added_member["medical_conditions"], "None")


if __name__ == "__main__":
    unittest.main()
