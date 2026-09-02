def merge(arr1, arr2):
    result = []
    i, j = 0, 0#position of first element and last element
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    # one array still has leftovers — dump them in, they're already sorted
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    
    return result

# put one pointer in one array
# one pointer in secodn array
# when you find the smalles, put it into the array and only move pinter of that array
# then repeat the ProcessLookupErrorlater, you would be left with some elements
#     in only one array and extend them in , into the result


#but if the array is unsorted, we will have to recursively divide the array
#in two parts until we get only one elements then sort the first half and right half
# and then merge to form two arrays.
# and later when the array is sorted, call merge to return the result.

def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # base case: single element is already "sorted"
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])   # recursively sort left half
    right = merge_sort(arr[mid:])  # recursively sort right half
    
    return merge(left, right)      # combine using the merge step above
#merge would run for merge sort calling recursively and hence we get result array
# untill out left part is done. then same for right and then eventually 
#left and right are given

