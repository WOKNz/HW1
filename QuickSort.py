def default_key(x):   # default key: use the value as-is
    return x


def quick_sort(a, key=default_key):  # interface
    quick_sort2(a, 0, len(a)-1, key=key)


def quick_sort2(a, low, high, key=default_key):  # split list
    if low < high:  # stop call for list of 1
        split = partition(a, low, high, key=key)  # split index
        quick_sort2(a, low, split-1, key=key)  # left side
        quick_sort2(a, split + 1, high, key=key)  # right side


def partition(a, low, high, key=default_key):  # setting the pivot
    pivot_idx = get_pivot(a, low, high, key=key)
    pivot_val = a[pivot_idx]
    a[pivot_idx], a[low] = a[low], a[pivot_idx]  # swap
    border = low

    for i in range(low, high+1):  # comparing to pivot
        if key(a[i]) < key(pivot_val):
            border += 1
            a[i], a[border] = a[border], a[i]
    a[low], a[border] = a[border], a[low]
    return border


def get_pivot(a, low, high, key=default_key):  # selecting best pivot
    middle = (high + low) // 2
    pivot = high
    if key(a[low]) < key(a[middle]):
        if key(a[middle]) < key(a[high]):
            pivot = middle
    elif key(a[low]) < key(a[high]):
        pivot = low
    return pivot

