from views.dashboard_view import DashboardView

class DashboardController:
    def __init__(self, members, appointments, trainers, attendance_records):
        self.members = members
        self.appointments = appointments
        self.trainers = trainers
        self.attendance_records = attendance_records

    def generate_membership_metrics(self):
        metrics = {
            "total_members": len(self.members),
            "regular_members": sum(1 for m in self.members if m["membership_type"] == "Regular"),
            "premium_members": sum(1 for m in self.members if m["membership_type"] == "Premium"),
            "trial_members": sum(1 for m in self.members if m["membership_type"] == "Trial"),
        }
        DashboardView.display_membership_metrics(metrics)

    def generate_revenue_trends(self):
        revenue_data = {
            "January": 5000,
            "February": 6000,
            "March": 7500,
        }
        DashboardView.display_revenue_trends(revenue_data)

    def view_trainer_schedule(self, trainer_id):
        trainer = self.trainers.get(trainer_id)
        if trainer:
            DashboardView.display_trainer_schedule(trainer)
        else:
            print("Trainer not found.")

    def generate_peak_hours(self):
        peak_hours_data = {
            "6 AM": 20,
            "7 AM": 25,
            "6 PM": 30,
            "7 PM": 35,
        }
        DashboardView.display_peak_hours(peak_hours_data)
