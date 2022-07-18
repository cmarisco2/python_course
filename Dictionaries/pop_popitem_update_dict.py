# test dictionary

gamertag = dict(name="cmarisco", id=12345, isCool=False, kills=200, champ=True)
print("gamertag")
print(gamertag)

# demo pop()
print("pop champ")
gamertag.pop('champ')
print(gamertag)

# demo popitem

print("pop random key")
gamertag.popitem()
print(gamertag)

# demo update

xbox_tag = dict(name="jon", id=23455, kills=10, champ=False, city='denver')
print("xbox tag")
print(xbox_tag)

print('update gamertag with xbox_tag fields: ')
gamertag.update(xbox_tag)
print("new gamertag:")
print(gamertag)
