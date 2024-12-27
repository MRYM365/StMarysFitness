import matplotlib.pyplot as plt

class DashboardView:
    @staticmethod
    def display_membership_metrics(metrics):
        print("\nMembership Metrics:")
        print(f"Total Members: {metrics['total_members']}")
        print(f"Regular Members: {metrics['regular_members']}")
        print(f"Premium Members: {metrics['premium_members']}")
        print(f"Trial Members: {metrics['trial_members']}")

    @staticmethod
    def display_revenue_trends(revenue_data):
        print("\nRevenue Trends:")
        for period, revenue in revenue_data.items():
            print(f"{period}: ${revenue}")

        # Example chart for revenue trends
        plt.bar(revenue_data.keys(), revenue_data.values())
        plt.title("Revenue Trends")
        plt.xlabel("Time Period")
        plt.ylabel("Revenue")
        plt.show()

    @staticmethod
    def display_trainer_schedule(trainer):
        print(f"\nSchedule for Trainer {trainer.name}:")
        for appointment in trainer.view_schedule():
            print(f" - {appointment.date}: {appointment.activity}")

    @staticmethod
    def display_peak_hours(peak_hours_data):
        print("\nPeak Gym Hours:")
        for hour, count in peak_hours_data.items():
            print(f"{hour}: {count} members")
