class PlaybackHistory:
    def __init__(self):
        self.history = []

    def play(self, song_name):
        self.history.append(song_name)
        print(f"Playing {song_name}...")

    def undo_last_play(self):
        if self.history:
            song = self.history.pop()
            print(f"Undo last play: {song}")
        else:
            print("No playback history.")
