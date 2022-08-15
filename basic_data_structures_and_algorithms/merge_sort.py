
# Big Help to fix bugs from link below!
# https: // github.com/chen0040/pyalgs/blob/master/pyalgs/algorithms/commons/sorting.py

# define merge and merge sort
import random


"""
    Merge function requires 3 key pieces of attention
    1) hi -> passed in as len(arr) - 1
        -Need hi + 1 in the range to include all indices
        -Means only for loop needs adjusting but all else is normal
    2) cpy arr in this function 
        -Ensures an update to the moved values occurs in cpy
    3) j = mid + 1
        -Ensures correct index position for the merging arrays
    4) i > mid AND j > hi
        -Ensure no funky indice errors on merging
"""


def _merge(arr, lo, mid, hi):
    i = lo
    j = mid + 1

    # copy the array to the aux array in order
    aux = arr[::]

    # ensure range is hi + 1 (len()-1 is passed, need hi to be inclusive)
    for k in range(lo, hi + 1):
        # range check is GREATER than MID
        if i > mid:
            arr[k] = aux[j]
            j += 1
        # range check is GREATER than HI
        elif j > hi:
            arr[k] = aux[i]
            i += 1
        elif aux[i] < aux[j]:
            arr[k] = aux[i]
            i += 1
        else:
            arr[k] = aux[j]
            j += 1

# recursive function built well!


def _sort(arr, lo, hi):
    if hi <= lo:
        return
    mid = lo + (hi - lo) // 2
    _sort(arr, lo, mid)
    _sort(arr, mid + 1, hi)
    _merge(arr, lo, mid, hi)


def mergeSort(arr):
    _sort(arr, 0, len(arr) - 1)


nums = list(range(random.randint(0, 20)))
random.shuffle(nums)

print(nums)

mergeSort(nums)
print(nums)
