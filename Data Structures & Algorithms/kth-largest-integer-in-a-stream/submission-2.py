import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)

        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        if not self.nums:
            heapq.heappush(self.nums, val)

        elif val > self.nums[0]:
            if len(self.nums) >= self.k:
                heapq.heappop(self.nums)
            heapq.heappush(self.nums, val)
            # print(self.nums)

        return self.nums[0]

        # Time complexity: O(mlogk)     Space complexity: O(k)


