from models.workout_zone import WorkoutZone
from views.workout_zone_view import WorkoutZoneView

class WorkoutZoneController:
    def __init__(self):
        self.zones = {}

    def add_zone(self, zone_id, zone_name):
        if zone_id not in self.zones:
            zone = WorkoutZone(zone_id, zone_name)
            self.zones[zone_id] = zone
            print("Workout Zone added successfully!")
        else:
            print("Zone ID already exists.")

    def add_equipment_to_zone(self, zone_id, equipment):
        if zone_id in self.zones:
            self.zones[zone_id].add_equipment(equipment)
        else:
            print("Zone not found.")

    def remove_equipment_from_zone(self, zone_id, equipment):
        if zone_id in self.zones:
            self.zones[zone_id].remove_equipment(equipment)
        else:
            print("Zone not found.")

    def assign_attendant_to_zone(self, zone_id, attendant):
        if zone_id in self.zones:
            self.zones[zone_id].assign_attendant(attendant)
        else:
            print("Zone not found.")

    def display_zone(self, zone_id):
        if zone_id in self.zones:
            WorkoutZoneView.display_zone_details(self.zones[zone_id])
        else:
            print("Zone not found.")
