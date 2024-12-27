import unittest
from models.attendance import Attendance

class TestAttendance(unittest.TestCase):
    def test_create_attendance(self):
        attendance = Attendance(1, "Alice", "2024-01-15 10:00", "Cardio")
        self.assertEqual(attendance.attendance_id, 1)
        self.assertEqual(attendance.member, "Alice")
        self.assertEqual(attendance.date, "2024-01-15 10:00")
        self.assertEqual(attendance.activity, "Cardio")

if __name__ == "__main__":
    unittest.main()
