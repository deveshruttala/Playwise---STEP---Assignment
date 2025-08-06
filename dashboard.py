class Dashboard:
    def __init__(self, playlist, history, rating_tree, lookup):
        self.playlist = playlist
        self.history = history
        self.rating_tree = rating_tree
        self.lookup = lookup

    def snapshot(self):
        print("\n--- Dashboard Snapshot ---")
        print("Top 5 Longest Songs:")
        sorted_songs = sorted(self.playlist.songs, key=lambda s: s.duration, reverse=True)[:5]
        for song in sorted_songs:
            print(f"{song.name} ({song.duration}s)")

        print("\nRecently Played:")
        for song in reversed(self.history.history[-5:]):
            print(song)

        print("\nSong Count by Rating (approx.):")
        count = {}
        def _count(node):
            if not node:
                return
            count[node.rating] = count.get(node.rating, 0) + 1
            _count(node.left)
            _count(node.right)

        _count(self.rating_tree.root)
        print(count)
