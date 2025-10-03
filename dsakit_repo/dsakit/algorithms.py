from typing import List
def linear_search(arr: List, target) -> int:
    for i, v in enumerate(arr):
        if v == target: return i
    return -1
def binary_search(sorted_arr: List[int], target: int) -> int:
    lo, hi = 0, len(sorted_arr)-1
    while lo <= hi:
        mid = (lo+hi)//2
        if sorted_arr[mid] == target: return mid
        if sorted_arr[mid] < target: lo = mid+1
        else: hi = mid-1
    return -1
def bubble_sort(arr: List[int]) -> List[int]:
    a = arr[:]; n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]; swapped = True
        if not swapped: break
    return a
