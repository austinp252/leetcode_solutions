class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ''
        length = self.getShortestStringLength(strs)
        for i in range(0, length):  # max is shortest string length
            common = strs[0][i]
            for j in range(1, len(strs)):  # checks all strings
                if(strs[j][i] != common):
                    return prefix
            prefix += common
        return prefix

    def getShortestStringLength(self, strs):
        sLen = len(strs[0])
        for i in range(1, len(strs)):
            sLen = len(strs[i]) if len(strs[i]) < sLen else sLen
        return sLen
