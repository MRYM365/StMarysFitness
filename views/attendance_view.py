class AttendanceView:
    @staticmethod
    def display_attendance_details(attendance):
        print(f"Attendance ID: {attendance.attendance_id}")
        print(f"Member: {attendance.member.name}")
        print(f"Date: {attendance.date}")
        print(f"Activity: {attendance.activity}")

    @staticmethod
    def get_attendance_input():
        member_id = input("Enter Member ID: ")
        date = input("Enter Attendance Date and Time (YYYY-MM-DD HH:MM): ")
        activity = input("Enter Activity (e.g., Group Class, Cardio, Strength Training): ")
        return member_id, date, activity
