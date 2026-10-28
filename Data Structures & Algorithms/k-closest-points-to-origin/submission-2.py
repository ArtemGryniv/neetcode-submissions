import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances_heap = []

        for coord in points:
            x = coord[0]
            y = coord[1]
            distance = (((x - 0) ** 2) + ((y - 0) ** 2))
            heapq.heappush(distances_heap, (-1 * distance, coord))
            
            if len(distances_heap) > k:
                heapq.heappop(distances_heap)



        out = []
        while k > 0:
            distance, coord = heapq.heappop(distances_heap)
            out.append(coord)
            k -= 1

        return out