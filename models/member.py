from enum import Enum

class MembershipType(Enum):
    REGULAR = "Regular"
    PREMIUM = "Premium"
    TRIAL = "Trial"

class Member:
    def __init__(self, member_id, name, membership_type):
        self.member_id = member_id
        self.name = name
        self.membership_type = membership_type
        self.health_info = {}
        self.appointments = []

    def add_appointment(self, appointment):
        self.appointments.append(appointment)

    def cancel_appointment(self, appointment_id):
        self.appointments = [
            appointment for appointment in self.appointments
            if appointment.appointment_id != appointment_id
        ]
