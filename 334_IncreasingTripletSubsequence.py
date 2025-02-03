class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        first, second = float("inf"),float("inf")
        for idx in range(len(nums)):
            if first >= nums[idx]:
                first = nums[idx]

            elif second >= nums[idx] > first:
                second = nums[idx]

            elif nums[idx] > second:
                return True
    
        return False
    