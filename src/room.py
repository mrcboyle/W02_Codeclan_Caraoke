class Room:
    def __init__(self, room_no, capacity, entry_fee):
        self.room_no = room_no
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.guests = []
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        self.songs.remove(song)