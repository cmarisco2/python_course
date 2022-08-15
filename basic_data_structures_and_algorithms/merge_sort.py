# https: // github.com/chen0040/pyalgs/blob/master/pyalgs/algorithms/commons/sorting.py

# define merge and merge sort
from random import shuffle
nums = [5, 9, 11, 3, 4, 6]

shuffle(nums)
print(nums)

# array partitioned by 2 sub-arrays of equal length.
# the result is a single merged array in ascending order


def _merge(arr, lo, mid, hi):

    # copy the array to the aux array in order
    aux = arr[::1]

    i = lo
    j = mid + 1

    for k in range(lo, hi + 1):
        if i > mid:
            arr[k] = aux[j]
            j += 1
        elif j > hi:
            arr[k] = aux[i]
            i += 1
        elif aux[i] < aux[j]:
            arr[k] = aux[i]
            i += 1
        else:
            arr[k] = aux[j]
            j += 1


def _sort(arr, lo, hi):
    if hi <= lo:
        return
    mid = lo + (hi - lo) // 2
    print(mid)
    _sort(arr,  lo, mid)
    _sort(arr,   mid + 1, hi)
    _merge(arr,  lo, mid, hi)


def mergeSort(arr):
    _sort(arr,  0, len(arr) - 1)


# aux = nums[::1]
# _merge(nums, aux, 0, len(nums)//2, len(aux))
mergeSort(nums)
print(nums)
