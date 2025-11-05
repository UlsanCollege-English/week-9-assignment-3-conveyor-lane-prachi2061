import heapq

def sort_k_sorted(arr, k):
    if not arr:
        return []

    result = []
    heap = []

    for i in range(min(k + 1, len(arr))):
        heapq.heappush(heap, arr[i])

    for i in range(k + 1, len(arr)):
        heapq.heappush(heap, arr[i])
        result.append(heapq.heappop(heap))

    while heap:
        result.append(heapq.heappop(heap))

    return result