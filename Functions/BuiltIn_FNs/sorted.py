# demo sorted w/ key word arguments reverse and key

song_list = [
    {'title': 'Without Me', 'play_count': 100},
    {'title': 'In Da Club', 'play_count': 200},
    {'title': 'N95', 'play_count': 150}
]

print(f"Song list Object: {song_list}")

sorted_by = sorted(song_list, key=lambda song: song['title'])

print(f"Songs sorted by title: {sorted_by}")

sorted_by = sorted(
    song_list, key=lambda song: song['play_count'], reverse=True
)
print(f"Songs sorted by play count: {sorted_by}")
