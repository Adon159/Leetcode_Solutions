class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check = set(nums)
        if len(check) != len(nums):
            return True
        else:
            return False