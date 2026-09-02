#refer others/mergesort for merge sort logic, and inversion is 
#when i<j but arr[i]>arr[j], index at which the element exists
# is less than next but next element is greater.
# # so inversion would be left +right + actual split(when i have actual left and right)
# 3 i am calling actual left and right, those array which are seperated when the
# function call starts, when array is divided by mid position
def merge_and_count(arr1, arr2):
    result = []
    i, j = 0, 0
    inversions = 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
            inversions += len(arr1) - i   # <-- key line
    
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    
    return result, inversions

def merge_sort_and_count(arr):
    if len(arr) <= 1:
        return arr, 0
    
    mid = len(arr) // 2
    left, inv_left = merge_sort_and_count(arr[:mid])
    right, inv_right = merge_sort_and_count(arr[mid:])
    merged, inv_split = merge_and_count(left, right)
    
    return merged, inv_left + inv_right + inv_split