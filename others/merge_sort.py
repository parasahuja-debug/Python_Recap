def merge(arr1, arr2):
    result = []
    i, j = 0, 0
    
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