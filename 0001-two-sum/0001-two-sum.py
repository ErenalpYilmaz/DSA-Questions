class Solution(object):
    def twoSum(self, nums, target, ):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if i != j+1:
                    if nums[i] + nums[j+1] == target:
                        result.append(i)
                        result.append(j+1)
                        return result