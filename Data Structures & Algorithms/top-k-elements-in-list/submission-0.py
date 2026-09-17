class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        bucket = [[] for i in range(len(nums) + 1)]
        res = []

        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Insert the counts in the bucket
        for num, count in count.items():
            bucket[count].append(num)

        for lst in bucket[::-1]:
            if k == 0:
                return res

            for num in lst:
                res.append(num)
                k -= 1
