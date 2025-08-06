from playlist_engine import Playlist
from playback_history import PlaybackHistory
from song_rating_tree import SongRatingTree
from song_lookup import SongLookup
from sorting import merge_sort
from dashboard import Dashboard

playlist = Playlist()
history = PlaybackHistory()
rating_tree = SongRatingTree()
lookup = SongLookup()
dashboard = Dashboard(playlist, history, rating_tree, lookup)

def show_menu():
    print("\n--- PlayWise CLI Menu ---")
    print("1. Add song to playlist")
    print("2. Delete song from playlist")
    print("3. Move song")
    print("4. Reverse playlist")
    print("5. Play a song")
    print("6. Undo last playback")
    print("7. Show playlist")
    print("8. Rate a song")
    print("9. Search songs by rating")
    print("10. Get song metadata")
    print("11. Sort playlist by duration")
    print("12. Show dashboard snapshot")
    print("0. Exit")

while True:
    show_menu()
    choice = input("Enter choice: ")

    if choice == '1':
        name = input("Song name: ")
        artist = input("Artist: ")
        duration = int(input("Duration (in sec): "))
        playlist.add_song(name, artist, duration)
        lookup.add_song(name, artist, duration)
        print("Song added.")

    elif choice == '2':
        name = input("Enter song name to delete: ")
        playlist.delete_song(name)

    elif choice == '3':
        name = input("Song name to move: ")
        pos = int(input("New position: "))
        playlist.move_song(name, pos)

    elif choice == '4':
        playlist.reverse_playlist()

    elif choice == '5':
        name = input("Song to play: ")
        history.play(name)

    elif choice == '6':
        history.undo_last_play()

    elif choice == '7':
        playlist.show_playlist()

    elif choice == '8':
        name = input("Song name to rate: ")
        rating = int(input("Rating (1-5): "))
        rating_tree.insert(name, rating)

    elif choice == '9':
        rating = int(input("Search songs with rating: "))
        rating_tree.search_by_rating(rating)

    elif choice == '10':
        name = input("Song name for metadata: ")
        lookup.get_metadata(name)

    elif choice == '11':
        playlist.songs = merge_sort(playlist.songs)
        print("Playlist sorted by duration.")

    elif choice == '12':
        dashboard.snapshot()

    elif choice == '0':
        break

    else:
        print("Invalid choice. Try again.")
