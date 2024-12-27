from controllers.member_controller import MemberController
from views.member_view import MemberView
from controllers.workout_zone_controller import WorkoutZoneController
from views.workout_zone_view import WorkoutZoneView
from controllers.appointment_controller import AppointmentController
from views.appointment_view import AppointmentView
from controllers.subscription_controller import SubscriptionController
from controllers.payment_controller import PaymentController
from views.payment_view import PaymentView
from controllers.attendance_controller import AttendanceController
from views.attendance_view import AttendanceView
from controllers.dashboard_controller import DashboardController

def main():
    controller = MemberController()

    # Adding a new member
    print("Add a new member:")
    name, membership_type = MemberView.get_member_input()
    controller.add_member(member_id=1, name=name, membership_type=membership_type)

    # Displaying member details
    print("\nMember Details:")
    controller.display_member(member_id=1)

    # Updating health information
    print("\nUpdating Health Info:")
    health_info = {"weight": 75, "height": 180}
    controller.update_member_health_info(member_id=1, health_info=health_info)

    # Displaying updated member details
    print("\nUpdated Member Details:")
    controller.display_member(member_id=1)


def main():
    # Initialize WorkoutZoneController
    zone_controller = WorkoutZoneController()

    # Add a new zone
    zone_name = WorkoutZoneView.get_zone_input()
    zone_controller.add_zone(1, zone_name)

    # Add equipment to the zone
    equipment = WorkoutZoneView.get_equipment_input()
    zone_controller.add_equipment_to_zone(1, equipment)

    # Assign an attendant
    attendant = WorkoutZoneView.get_attendant_input()
    zone_controller.assign_attendant_to_zone(1, attendant)

    # Display zone details
    zone_controller.display_zone(1)

def main():
    # Initialize AppointmentController
    appointment_controller = AppointmentController()

    # Schedule a new appointment
    print("Schedule a new appointment:")
    member_id, trainer, appointment_type, date = AppointmentView.get_appointment_input()
    appointment_controller.schedule_appointment(1, member_id, trainer, appointment_type, date)

    # Display the appointment
    print("\nAppointment Details:")
    appointment_controller.display_appointment(1)

    # Reschedule the appointment
    print("\nRescheduling the appointment:")
    new_date = AppointmentView.get_reschedule_input()
    appointment_controller.reschedule_appointment(1, new_date)

    # Display the updated appointment
    print("\nUpdated Appointment Details:")
    appointment_controller.display_appointment(1)

def main():
    # Initialize Controllers
    subscription_controller = SubscriptionController()
    payment_controller = PaymentController()

    # Mock Member
    class MockMember:
        def __init__(self, name):
            self.name = name

    member = MockMember("Alice")

    # Create a Subscription
    print("Create a Subscription:")
    plan, fee, discount = PaymentView.get_subscription_input()
    subscription_controller.create_subscription(1, member, plan, fee, discount)

    # Display Subscription Details
    print("\nSubscription Details:")
    subscription_controller.display_subscription(1)

    # Process Payment
    print("\nProcess Payment:")
    _, amount, payment_method = PaymentView.get_payment_input()
    subscription = subscription_controller.subscriptions[1]
    payment_controller.process_payment(1, subscription, amount, payment_method)

    # Display Payment Details
    print("\nPayment Details:")
    payment_controller.display_payment(1)

def main():
    # Initialize AttendanceController
    attendance_controller = AttendanceController()

    # Mock Member
    class MockMember:
        def __init__(self, name):
            self.name = name

    member = MockMember("Alice")
    attendance_controller.member_lookup["1"] = member

    # Log a new attendance record
    print("Log Attendance:")
    member_id, date, activity = AttendanceView.get_attendance_input()
    attendance_controller.log_attendance(1, member_id, date, activity)

    # Display the attendance record
    print("\nAttendance Details:")
    attendance_controller.display_attendance(1)

    # Generate a report
    print("\nAttendance Report:")
    attendance_controller.generate_reports()

def main():
    # Mock data
    members = [
        {"membership_type": "Regular"},
        {"membership_type": "Premium"},
        {"membership_type": "Trial"},
        {"membership_type": "Premium"},
    ]
    trainers = {}
    appointments = []
    attendance_records = []

    # Initialize DashboardController
    dashboard_controller = DashboardController(members, appointments, trainers, attendance_records)

    # Generate metrics and reports
    print("\nGenerating Membership Metrics:")
    dashboard_controller.generate_membership_metrics()

    print("\nGenerating Revenue Trends:")
    dashboard_controller.generate_revenue_trends()

    print("\nGenerating Peak Hours Report:")
    dashboard_controller.generate_peak_hours()



if __name__ == "__main__":
    main()
