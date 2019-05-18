def default_key(x):   # default key:, key used to sort on different fields
    return x


def quick_sort(a, key=default_key):  # interface (better to use Unified call qs())
    quick_sort2(a, 0, len(a)-1, key=key)


def quick_sort2(a, low, high, key=default_key):  # split list
    if low < high:  # stop call for list of 1
        split = partition(a, low, high, key=key)  # split index
        quick_sort2(a, low, split-1, key=key)  # left side (recursive)
        quick_sort2(a, split + 1, high, key=key)  # right side (recursive)


def partition(a, low, high, key=default_key):  # setting the pivot
    pivot_idx = get_pivot(a, low, high, key=key)
    pivot_val = a[pivot_idx]
    a[pivot_idx], a[low] = a[low], a[pivot_idx]  # swap
    border = low

    for i in range(low, high+1):  # comparing to pivot
        if key(a[i]) < key(pivot_val):
            border += 1
            a[i], a[border] = a[border], a[i]  # swap
    a[low], a[border] = a[border], a[low]  # swap
    return border


def get_pivot(a, low, high, key=default_key):  # selecting best pivot of 3
    middle = (high + low) // 2
    pivot = high
    if key(a[low]) < key(a[middle]):
        if key(a[middle]) < key(a[high]):
            pivot = middle
    elif key(a[low]) < key(a[high]):
        pivot = low
    return pivot


def qs(listofobj, field: int, order: int):  # Unified call for sorting
    if field == 0 and order == 0:  # from small to large, on x
        quick_sort(listofobj, key=lambda point: point.x)
        return listofobj.copy()
    elif field == 0 and order == 1:  # from small to large, on y
        quick_sort(listofobj, key=lambda point: point.y)
        return listofobj.copy()
    elif field == 1 and order == 0:  # from large to small, on x
        quick_sort(listofobj, key=lambda point: point.x)
        tmp = []
        tmp = listofobj.copy()
        tmp.reverse()
        return tmp
    elif field == 1 and order == 1:  # from large to small, on y
        quick_sort(listofobj, key=lambda point: point.y)
        tmp = []
        tmp = listofobj.copy()
        tmp.reverse()
        return tmp
    else:  # Illegal input case
        print("One of the input parameters is illegal")
        return

