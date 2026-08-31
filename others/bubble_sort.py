def bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):#n-i-1 to compare j and j+1    
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
# compare one and its adjacent and swap