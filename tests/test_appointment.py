import unittest
from models.appointment import Appointment

class TestAppointment(unittest.TestCase):
    def test_create_appointment(self):
        appointment = Appointment(1, "Alice", "John Doe", "Personal Training", "2024-01-15 10:00")
        self.assertEqual(appointment.appointment_id, 1)
        self.assertEqual(appointment.trainer, "John Doe")
        self.assertEqual(appointment.appointment_type, "Personal Training")
        self.assertEqual(appointment.date, "2024-01-15 10:00")

    def test_reschedule(self):
        appointment = Appointment(1, "Alice", "John Doe", "Personal Training", "2024-01-15 10:00")
        appointment.reschedule("2024-01-16 11:00")
        self.assertEqual(appointment.date, "2024-01-16 11:00")

if __name__ == "__main__":
    unittest.main()
