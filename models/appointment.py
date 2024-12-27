class Appointment:
    def __init__(self, appointment_id, member, trainer, appointment_type, date):
        self.appointment_id = appointment_id
        self.member = member
        self.trainer = trainer
        self.appointment_type = appointment_type
        self.date = date

    def reschedule(self, new_date):
        self.date = new_date
