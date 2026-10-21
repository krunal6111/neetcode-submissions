import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Max heap
        heapq.heapify_max(nums)
        while k:
            n = heapq.heappop_max(nums) # heappop method is for min heap only, hence we use heappop_max
            k -= 1
            if k == 0:
                return n

        # Time complexity: O(nlogn)     # Space complexity: O(n)