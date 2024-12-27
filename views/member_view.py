from models.member import MembershipType

class MemberView:
    @staticmethod
    def display_member_details(member):
        print(f"Member ID: {member.member_id}")
        print(f"Name: {member.name}")
        print(f"Membership Type: {member.membership_type.value}")
        print(f"Health Info: {member.health_info}")
        print(f"Appointments: {len(member.appointments)}")

    @staticmethod
    def get_member_input():
        name = input("Enter Member Name: ")
        membership_type = input("Enter Membership Type (Regular/Premium/Trial): ").upper()
        return name, MembershipType[membership_type]
