class SongLookup:
    def __init__(self):
        self.db = {}

    def add_song(self, name, artist, duration):
        self.db[name] = {"artist": artist, "duration": duration}

    def get_metadata(self, name):
        if name in self.db:
            data = self.db[name]
            print(f"{name} by {data['artist']} ({data['duration']}s)")
        else:
            print("Song not found.")
