# Fuse Inheritance and Special Methods for cool functionality:

# init not called here -> MRO, calls the super class init()
class GrumpyDict(dict):
    # add a print statement ahead of the normal repr
    def __repr__(self) -> str:
        print("None Of Your Business")
        return super().__repr__()

    # add a print statement vice sending none/null/false
    def __missing__(self, key):
        return f"You Want {key}? Well, it ain't HERE!"

    def __setitem__(self, __k, __v) -> None:
        print("You're always changing things")
        print("Fine, as you wish.... :(")
        return super().__setitem__(__k, __v)


data = GrumpyDict({"first": "Tom", "animal": "cat"})

print(data)
print(data['dog'])
data['protagonist'] = 'Eren Jaegar'
print(data)
