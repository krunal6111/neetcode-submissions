import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # convert to negative for a max heap
        neg_stones = [-x for x in stones]
        heapq.heapify(neg_stones)

        while len(neg_stones) > 1:
            x = -1 * heapq.heappop(neg_stones)
            y = -1 * heapq.heappop(neg_stones)

            weight = max(x, y) - min(x, y)
            if weight != 0:
                heapq.heappush(neg_stones, -1 * weight)
            elif len(neg_stones) == 0:
                heapq.heappush(neg_stones, 0)

        return -1 * neg_stones[0]

        # Time complexity: O(n)     Space complexity: O(n)

        # We get O(n) time complexity cause we have used a loop to convert every value into negative integer. 