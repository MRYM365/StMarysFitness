class AppointmentView:
    @staticmethod
    def display_appointment_details(appointment):
        print(f"Appointment ID: {appointment.appointment_id}")
        print(f"Member: {appointment.member.name}")
        print(f"Trainer: {appointment.trainer}")
        print(f"Type: {appointment.appointment_type}")
        print(f"Date: {appointment.date}")

    @staticmethod
    def get_appointment_input():
        member_id = input("Enter Member ID: ")
        trainer = input("Enter Trainer Name: ")
        appointment_type = input("Enter Appointment Type (e.g., Personal Training, Group Class): ")
        date = input("Enter Appointment Date and Time (YYYY-MM-DD HH:MM): ")
        return member_id, trainer, appointment_type, date

    @staticmethod
    def get_reschedule_input():
        new_date = input("Enter New Appointment Date and Time (YYYY-MM-DD HH:MM): ")
        return new_date
