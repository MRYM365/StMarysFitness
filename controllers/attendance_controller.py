from models.attendance import Attendance
from views.attendance_view import AttendanceView

class AttendanceController:
    def __init__(self):
        self.attendance_records = {}
        self.member_lookup = {}  # Placeholder for member lookup

    def log_attendance(self, attendance_id, member_id, date, activity):
        # Mock member lookup
        if member_id in self.member_lookup:
            member = self.member_lookup[member_id]
        else:
            print("Member not found.")
            return

        attendance = Attendance(attendance_id, member, date, activity)
        self.attendance_records[attendance_id] = attendance
        print("Attendance logged successfully!")

    def display_attendance(self, attendance_id):
        if attendance_id in self.attendance_records:
            AttendanceView.display_attendance_details(self.attendance_records[attendance_id])
        else:
            print("Attendance record not found.")

    def generate_reports(self):
        # Example: Count attendance by activity
        activity_count = {}
        for attendance in self.attendance_records.values():
            activity_count[attendance.activity] = activity_count.get(attendance.activity, 0) + 1

        print("Attendance Report:")
        for activity, count in activity_count.items():
            print(f"Activity: {activity}, Count: {count}")
