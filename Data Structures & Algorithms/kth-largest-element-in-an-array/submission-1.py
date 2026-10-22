class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l, r):
            pivot, p = nums[r], l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = pivot, nums[p]

            if k < p: return quickSelect(l, p-1)
            elif k > p:return quickSelect(p + 1, r)
            else:
                return nums[k]

        
        return quickSelect(0, len(nums) - 1)

        # Time complexity: O(n) for avarage case    Space complexity: O(n)
                        #  O(n^2) for worst case