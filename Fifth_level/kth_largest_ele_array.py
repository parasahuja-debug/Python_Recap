# import heapq

# def kth_largest(arr, k):
#     heap = []

#     for num in arr:
#         heapq.heappush(heap, num)
#         print(heap)
#         if len(heap) > k:
#             heapq.heappop(heap)  # remove smallest
#             print(heap)
#     return heap[0]  # kth largest

# print(kth_largest([1,2,3,5,6,7], 3))

import heapq

def kth_smallest(arr, k):
    heap = []

    for num in arr:
        heapq.heappush(heap, -num)   # push negative → max heap
        print(heap)
        if len(heap) > k:
            heapq.heappop(heap)      # remove largest (most negative)
            print(heap)
    return -heap[0]  # kth smallest

print(kth_smallest([1,2,3,5,6,7], 3))