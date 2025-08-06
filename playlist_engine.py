class Song:
    def __init__(self, name, artist, duration):
        self.name = name
        self.artist = artist
        self.duration = duration

class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, name, artist, duration):
        self.songs.append(Song(name, artist, duration))

    def delete_song(self, name):
        self.songs = [s for s in self.songs if s.name != name]

    def move_song(self, name, position):
        song = next((s for s in self.songs if s.name == name), None)
        if song:
            self.songs.remove(song)
            self.songs.insert(position, song)

    def reverse_playlist(self):
        self.songs.reverse()

    def show_playlist(self):
        for song in self.songs:
            print(f"> {song.name} by {song.artist} ({song.duration}s)")
