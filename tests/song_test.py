import unittest
from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("Sweet Caroline", "Neil Diamond")
        self.song2 = Song("Born To Run", "Bruce Springstein")
        self.song3 = Song("Love Shack", "B-52s")
        self.song4 = Song("Stand By Me", "Ben E King")
        self.song5 = Song("Purple Rain", "Prince")

    def test_song_has_title(self):
        self.assertEqual("Love Shack", self.song3.title)

    def test_song_has_artist(self):
        self.assertEqual("Prince", self.song5.artist)