class WorkoutZone:
    def __init__(self, zone_id, zone_name):
        self.zone_id = zone_id
        self.zone_name = zone_name
        self.equipment_list = []
        self.attendant = None

    def add_equipment(self, equipment):
        if equipment not in self.equipment_list:
            self.equipment_list.append(equipment)
        else:
            print(f"{equipment} is already in the equipment list.")

    def remove_equipment(self, equipment):
        if equipment in self.equipment_list:
            self.equipment_list.remove(equipment)
        else:
            print(f"{equipment} is not found in the equipment list.")

    def assign_attendant(self, attendant):
        self.attendant = attendant
