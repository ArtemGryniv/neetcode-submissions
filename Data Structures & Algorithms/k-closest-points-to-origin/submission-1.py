import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances_heap = []

        for coord in points:
            x = coord[0]
            y = coord[1]
            distance = (((x - 0) ** 2) + ((y - 0) ** 2))
            distances_heap.append((distance, coord))

        heapq.heapify(distances_heap)

        out = []
        while k > 0:
            distance, coord = heapq.heappop(distances_heap)
            out.append(coord)
            k -= 1

        return out