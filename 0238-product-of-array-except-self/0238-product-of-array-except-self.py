class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            result_multiply = 1
            for j in range(len(nums)):
                if j != i:
                    result_multiply*= nums[j]

            result.append(result_multiply)
            
        return result