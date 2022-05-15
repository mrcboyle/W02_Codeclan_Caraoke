import unittest
from src.room import Room
from src.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room1 = Room(1, 5, 10.00)
        self.room2 = Room(2, 10, 15.00)
        self.room3 = Room(3, 10, 15.00)

    def test_room_has_number(self):
        self.assertEqual(1, self.room1.room_no)

    def test_room_has_capacity(self):
        self.assertEqual(10, self.room2.capacity)

    def test_room_has_entry_fee(self):
        self.assertEqual(15.00, self.room3.entry_fee)               

    def test_can_add_song(self):
        self.room.add_song(Song(self.song2.title))
        self.assertEqual(1, len(self.songs))

    # def test_can_remove_song(self):
    #     self.remove_song(self.)
    #     self.assertEqual(1, self.room.len(self.songs))
