from models.member import Member, MembershipType
from views.member_view import MemberView

class MemberController:
    def __init__(self):
        self.members = {}

    def add_member(self, member_id, name, membership_type):
        member = Member(member_id, name, membership_type)
        self.members[member_id] = member
        print("Member added successfully!")

    def update_member_health_info(self, member_id, health_info):
        if member_id in self.members:
            self.members[member_id].health_info = health_info
            print("Health information updated!")
        else:
            print("Member not found!")

    def display_member(self, member_id):
        if member_id in self.members:
            MemberView.display_member_details(self.members[member_id])
        else:
            print("Member not found!")
