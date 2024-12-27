class WorkoutZoneView:
    @staticmethod
    def display_zone_details(zone):
        print(f"Zone ID: {zone.zone_id}")
        print(f"Zone Name: {zone.zone_name}")
        print(f"Equipment List: {', '.join(zone.equipment_list) if zone.equipment_list else 'No equipment'}")
        print(f"Attendant: {zone.attendant if zone.attendant else 'No attendant assigned'}")

    @staticmethod
    def get_zone_input():
        zone_name = input("Enter Workout Zone Name: ")
        return zone_name

    @staticmethod
    def get_equipment_input():
        equipment = input("Enter Equipment Name: ")
        return equipment

    @staticmethod
    def get_attendant_input():
        attendant = input("Enter Attendant Name: ")
        return attendant
