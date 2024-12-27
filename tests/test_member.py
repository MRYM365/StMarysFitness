import unittest
from models.member import Member, MembershipType

class TestMember(unittest.TestCase):
    def test_create_member(self):
        member = Member(1, "Alice", MembershipType.PREMIUM)
        self.assertEqual(member.member_id, 1)
        self.assertEqual(member.name, "Alice")
        self.assertEqual(member.membership_type, MembershipType.PREMIUM)

    def test_add_appointment(self):
        member = Member(1, "Alice", MembershipType.PREMIUM)
        member.add_appointment("Session1")
        self.assertEqual(len(member.appointments), 1)

    def test_cancel_appointment(self):
        member = Member(1, "Alice", MembershipType.PREMIUM)
        member.add_appointment("Session1")
        member.cancel_appointment("Session1")
        self.assertEqual(len(member.appointments), 0)

if __name__ == "__main__":
    unittest.main()
