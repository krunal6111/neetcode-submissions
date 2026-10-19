import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []

        h = []
        for point in points:
            distance = math.sqrt((point[0] ** 2) + (point[1] ** 2))
            heapq.heappush(h, (distance, point))

        for i in range(k):
            distance, point = heapq.heappop(h)
            res.append(point)

        return res

        # Time complexity: (klogn)      Space complexity:O(n)