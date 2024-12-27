from models.appointment import Appointment
from views.appointment_view import AppointmentView

class AppointmentController:
    def __init__(self):
        self.appointments = {}
        self.member_lookup = {}  # Placeholder for member lookup

    def schedule_appointment(self, appointment_id, member_id, trainer, appointment_type, date):
        # Mock member lookup
        if member_id in self.member_lookup:
            member = self.member_lookup[member_id]
        else:
            print("Member not found.")
            return

        appointment = Appointment(appointment_id, member, trainer, appointment_type, date)
        self.appointments[appointment_id] = appointment
        print("Appointment scheduled successfully!")

    def cancel_appointment(self, appointment_id):
        if appointment_id in self.appointments:
            del self.appointments[appointment_id]
            print("Appointment cancelled.")
        else:
            print("Appointment not found.")

    def reschedule_appointment(self, appointment_id, new_date):
        if appointment_id in self.appointments:
            self.appointments[appointment_id].reschedule(new_date)
            print("Appointment rescheduled.")
        else:
            print("Appointment not found.")

    def display_appointment(self, appointment_id):
        if appointment_id in self.appointments:
            AppointmentView.display_appointment_details(self.appointments[appointment_id])
        else:
            print("Appointment not found.")
