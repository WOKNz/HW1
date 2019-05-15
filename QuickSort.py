def quick_sort(a):  # interface
    quick_sort2(a, 0, len(a)-1)


def quick_sort2(a, low, high):  # split list
    if low < high:  # stop call for list of 1
        split = partition(a, low, high)  # split index
        quick_sort2(a, low, split-1)  # left side
        quick_sort2(a, split + 1, high)  # right side


def partition(a, low, high):  # setting the pivot
    pivot_idx = get_pivot(a, low, high)
    pivot_val = a[pivot_idx]
    a[pivot_idx], a[low] = a[low], a[pivot_idx]  # swap
    border = low

    for i in range(low, high+1):  # comparing to pivot
        if a[i] < pivot_val:
            border += 1
            a[i], a[border] = a[border], a[i]
    a[low], a[border] = a[border], a[low]
    return border


def get_pivot(a, low, high):  # selecting best pivot
    middle = (high + low) // 2
    pivot = high
    if a[low] < a[middle]:
        if a[middle] < a[high]:
            pivot = middle
    elif a[low] < a[high]:
        pivot = low
    return pivot

