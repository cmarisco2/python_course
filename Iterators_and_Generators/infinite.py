# Use generators to infinitely cycle music beats

def current_beat():
    beat = 1
    while beat < 5:
        if beat == 0:
            beat = 1
        yield beat
        beat = (beat + 1) % 5


my_beat = current_beat()
for num in range(0, 10):
    print(next(my_beat))
