# demo iterating over list w/ for loop

names = ["Eren", "Reiner", "Mikasa", "Armin", True, 100, 12.53]

for word in names:
    print(word)


# demo iterating list w/ while loop
nums = [1, 2, 3]
i = 0

while i < len(nums):
    print(nums[i] * nums[i])
    i += 1
