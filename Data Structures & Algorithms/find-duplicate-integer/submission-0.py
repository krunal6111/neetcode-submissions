class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Floyd's tortoise hare method
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        print("Both intersected at ", slow)
        slow2 = 0
        while True:
            if slow == slow2:
                return slow2
            slow2 = nums[slow2]
            slow = nums[slow]
