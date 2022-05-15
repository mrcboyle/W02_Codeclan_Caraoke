import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest1 = Guest("Dave Jones", 75.00)
        self.guest2 = Guest("Andrew Smith", 20.00)
        self.guest3 = Guest("Michael Simpson", 40.00)
        self.guest4 = Guest("Andrew Cameron", 7.00)
        self.guest5 = Guest("Sam Adams", 25.00)

    def test_guest_has_name(self):
        self.assertEqual("Andrew Smith", self.guest2.name)        

    def test_guest_has_wallet(self):
        self.assertEqual(20, self.guest2.wallet)  

    # def test_guest_can_afford_entry_fee(self):
    #     self.guest.can_afford_entry_fee(self.guest3)
    #     self.assertEqual(True, self.guest.wallet)
