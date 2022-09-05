import unittest
from contact import Contact

contact=Contact("User","User LastName","user@gmail.com","house",2)
class TestContact(unittest.TestCase):
    def test_contact(self):
        self.assertEqual(contact.first_name,"User")
        self.assertEqual(contact.last_name,"User LastName")
        self.assertEqual(contact.email,"user@gmail.com")
        self.assertEqual(contact.work_place,"house")
        self.assertEqual(contact.total_activities,2)
    
    def test_modify_contact(self):
        contact.first_name="User2"
        self.assertEqual(contact.first_name,"User2")

        contact.last_name="User2 Last_name"
        self.assertEqual(contact.last_name,"User2 Last_name")

        contact.email="user2@gmail.com"
        self.assertEqual(contact.email,"user2@gmail.com")

        contact.work_place="office"
        self.assertEqual(contact.work_place,"office")

        contact.total_activities=4
        self.assertEqual(contact.total_activities,4)

if __name__=='__main__':
    unittest.main()