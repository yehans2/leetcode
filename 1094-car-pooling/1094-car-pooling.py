class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t : t[1])
        minheap = []
        curpas = 0
        for t in trips:
            numpas, start, end = t
            while minheap and minheap[0][0] <= start:
                curpas -= minheap[0][1]
                heapq.heappop(minheap)
            curpas += numpas
            if curpas > capacity:
                return False
            heapq.heappush(minheap, [end, numpas])
        return True
            
        