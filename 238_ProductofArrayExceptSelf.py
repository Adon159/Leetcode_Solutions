class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ln = len(nums)
        final_list = [1] * n  # Initialize result array

        #SecondLoop
        temp = 1
        for i in range(ln):
            final_list[i] = temp
            temp *= nums[i]

        #FirstLoop
        temp = 1
        for i in range(ln-1,-1,-1):
            final_list[i] *= temp
            temp *= nums[i]


        return final_list
    
    # class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         m_idx = 0
#         loop_idx = 0
#         final_list = []
#         temp = 1

#         while m_idx < len(nums):
#             if loop_idx == len(nums):
#                 m_idx += 1
#                 loop_idx = 0
#                 final_list.append(temp)
#                 temp = 1

#             if m_idx != loop_idx:
#                 temp *= nums[loop_idx]
#                 loop_idx += 1

#             else:
#                 loop_idx +=1
        
#         return final_list

#Time Complexity O(n)
