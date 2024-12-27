import unittest
from models.workout_zone import WorkoutZone

class TestWorkoutZone(unittest.TestCase):
    def test_create_zone(self):
        zone = WorkoutZone(1, "Cardio")
        self.assertEqual(zone.zone_id, 1)
        self.assertEqual(zone.zone_name, "Cardio")

    def test_add_equipment(self):
        zone = WorkoutZone(1, "Cardio")
        zone.add_equipment("Treadmill")
        self.assertIn("Treadmill", zone.equipment_list)

    def test_remove_equipment(self):
        zone = WorkoutZone(1, "Cardio")
        zone.add_equipment("Treadmill")
        zone.remove_equipment("Treadmill")
        self.assertNotIn("Treadmill", zone.equipment_list)

    def test_assign_attendant(self):
        zone = WorkoutZone(1, "Cardio")
        zone.assign_attendant("John Doe")
        self.assertEqual(zone.attendant, "John Doe")

if __name__ == "__main__":
    unittest.main()
