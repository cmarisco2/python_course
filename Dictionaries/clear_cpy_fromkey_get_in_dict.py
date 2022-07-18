# demo basic dictionary methods and perform membership check

d = dict(a=1, b=2, c=3)
print(f"d is {d}")

# cpy demo
c = d.copy()
print(f"c is a copy of d: {c}")
print(f"c values equal d: {c==d}")
print(f"c is d: {c is d}")

# membership demo
print(f"membership check for key 'a'\nis 'a' in dictionary d: {'a' in d}")
print(f"value check for dictionary d. is 3 in d: {3 in d.values()}")

# clear demo
c.clear()
print(f"c after clear method: {c}")

# get demo
print(f"get(d) from d is: {d.get('d')}")
print(f"get(c) from d: {d.get('c')}")

# fromkeys demo
game_stats = ["kills", "lives", "wins", "losses", "high_score", "power_ups"]
print(f"list of game stats: {game_stats}")
print("Converting game stats into a mapping with default 0 values: ")

game_scores = {}.fromkeys(game_stats, 0)
print(game_scores)
