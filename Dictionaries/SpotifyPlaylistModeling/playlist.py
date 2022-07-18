# demo that combines list and dictionary concepts into one small example

# Playlist is just an obj/dict with key song-holding a list of songs

# songs list will have objects/dicts that have song titles, artist, etc.
# ie. each song is an object/dict

playlist = {
    'title': 'myFunk',
    'author': 'Chris',
    'songs': [
        {'title': 'song1', 'artist': ['blue'], 'duration': 2.5},
        {'title': 'song2', 'artist': ['kitty', 'djCat'], 'duration': 3.5},
        {'title': 'meowmeow', 'artist': ['Garfield'], 'duration': 2}
    ]
}

print(playlist)

total_duration = 0
for song in playlist['songs']:
    total_duration += song['duration']

print(
    f"total time duration of the music in the playlist is: {total_duration} minutes"
)
