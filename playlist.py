import datetime

class Song:
    def __init__(self, title, artist, genre, duration, release_year):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.duration = duration
        self.release_year = release_year

def merge_sort(songs, key):
    if len(songs) <= 1:
        return songs
    
    mid = len(songs) // 2
    left_half = songs[:mid]
    right_half = songs[mid:]

    left_half = merge_sort(left_half, key)
    right_half = merge_sort(right_half, key)

    return merge(left_half, right_half, key)

def merge(left, right, key):
    merged = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if getattr(left[left_index], key) < getattr(right[right_index], key):
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged

def create_personalized_playlist():
    print("\n" + "="*50)
    print("Welcome to the Personalized Playlist Sorting Program!")
    print("="*50)
    print("Create your personalized playlist. Type 'done' to finish.\n")
    
    playlist = []
    while True:
        song_name = input("Enter the name of the song: ").strip()
        if song_name.lower() == 'done':
            break
        artist = input("Enter the artist(s) of the song: ").strip()
        genre = input("Enter the genre of the song: ").strip()
        duration = input("Enter the duration of the song (mins secs): ").strip()
        release_year = input("Enter the release year of the song: ").strip()
        playlist.append(Song(song_name, artist, genre, duration, release_year))
    return playlist

def display_playlist(playlist):
    if not playlist:
        print("\nPlaylist is empty.")
        return
    
    print("\nYour Playlist:")
    print("-" * 50)
    for index, song in enumerate(playlist, start=1):
        print(f"{index}. {song.title} - {song.artist} ({song.genre}) [{song.duration}] ({song.release_year})")
        if index < len(playlist):  # Add a line between songs
            print("-" * 50)

def choose_attribute():
    print("\nChoose an attribute to sort the playlist:")
    print("1. Song Title")
    print("2. Artist")
    print("3. Genre")
    print("4. Duration")
    print("5. Release Year")
    choice = input("Enter your choice (1-5): ").strip()
    while choice not in ['1', '2', '3', '4', '5']:
        print("Invalid choice. Please enter a number between 1 and 5.")
        choice = input("Enter your choice (1-5): ").strip()
    return int(choice)

def choose_sort_order():
    print("\nChoose sorting order:")
    print("1. Ascending")
    print("2. Descending")
    choice = input("Enter your choice (1-2): ").strip()
    while choice not in ['1', '2']:
        print("Invalid choice. Please enter 1 or 2.")
        choice = input("Enter your choice (1-2): ").strip()
    return choice == '1'

def validate_duration(duration):
    parts = duration.split()
    if len(parts) != 2:
        return False
    try:
        mins = int(parts[0])
        secs = int(parts[1])
        if mins < 0 or secs < 0 or secs >= 60:
            return False
    except ValueError:
        return False
    return True

def validate_release_year(year):
    try:
        year = int(year)
        if year < 0 or year > datetime.datetime.now().year:
            return False
    except ValueError:  
        return False
    return True

def save_playlist(playlist, filename):
    with open(filename, 'w') as f:
        for song in playlist:
            f.write(f"{song.title} - {song.artist} ({song.genre}) [{song.duration}] ({song.release_year})\n")

def main():
    playlist = create_personalized_playlist()

    if not playlist:
        print("\nYou haven't entered any songs. Exiting.")
        return

    while True:
        print("\nOriginal Playlist:")
        display_playlist(playlist)

        attribute_index = choose_attribute()
        sort_key = None

        if attribute_index == 1:  # Song Title attribute
            sort_key = 'title'
        elif attribute_index == 2:  # Artist attribute
            sort_key = 'artist'
        elif attribute_index == 3:  # Genre attribute
            sort_key = 'genre'
        elif attribute_index == 4:  # Duration attribute
            sort_key = 'duration'
        elif attribute_index == 5:  # Release Year attribute
            sort_key = 'release_year'

        ascending = choose_sort_order()

        playlist = merge_sort(playlist, sort_key)

        if not ascending:
            playlist.reverse()

        print(f"\nSongs sorted by {sort_key} in {'ascending' if ascending else 'descending'} order:")
        display_playlist(playlist)

        filename = input("\nEnter a filename to save the sorted playlist (e.g., playlist.txt): ").strip()
        save_playlist(playlist, filename)
        print(f"\nPlaylist saved as '{filename}'.")

        create_new_playlist = input("\nDo you want to create a new playlist? (yes/no): ").strip().lower()
        if create_new_playlist== 'yes' or create_new_playlist=="y":
            continue
        else:
            break

if __name__ == "__main__":
    main()
