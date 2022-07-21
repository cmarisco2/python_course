# demo zip()

# Given 2 collections, zip and associate them in a list and in a dictionary
titles = ['wizard', 'president', 'archduke', 'tech lead', 'doctor']
personnel = ['gandalf', 'eisenhower', 'ferdinand', 'chris', 'Of_Thuganomics']

print(f"titles: {titles}\npeople: {personnel}")
print('zip titles and people as a tuple:')
fast_zip = zip(titles, personnel)
print(tuple(fast_zip))

fast_zip = zip(titles, personnel)
print('zip titles and people as a list:')
print(list(fast_zip))

fast_zip = zip(titles, personnel)
print('zip titles and people as a dictionary:')
print(dict(fast_zip))
