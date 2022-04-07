class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index1, i in enumerate(nums):
            partner = target - i
            if(partner in nums[index1+1:]):
                return([index1, nums[index1+1:].index(partner)+index1+1])
        return
