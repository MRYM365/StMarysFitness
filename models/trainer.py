class Trainer:
    def __init__(self, trainer_id, name):
        self.trainer_id = trainer_id
        self.name = name
        self.schedule = []  # List of appointments or classes

    def add_to_schedule(self, appointment):
        self.schedule.append(appointment)

    def view_schedule(self):
        return self.schedule
