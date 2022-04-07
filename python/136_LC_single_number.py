from collections import defaultdict


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visited = defaultdict(int)
        for item in nums:
            visited[item] += 1
        for item in nums:
            if visited[item] == 1:
                return item
