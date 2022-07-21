test1 = (80, 91, 78)
test2 = (98, 89, 53)
students = ('dan', 'ang', 'kate')

final_scores = {thing[0]: max(thing[1], thing[2])
                for thing in zip(students, test1, test2)}
print(final_scores)
