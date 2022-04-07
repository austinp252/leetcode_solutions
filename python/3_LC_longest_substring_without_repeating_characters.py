class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # with front and end counters, should be O(n)

        maxLength = 0
        startIndex = 0
        for index, char in enumerate(s):
            # iterate each character
            # keep track of current items in word
            # can use 'is in', will take longer
            # if this character is not in word, add new char to word
            # if this character is in word, iterate start index until this condition is true
            # while loop here?
            # issue: this substring is 1 char before desired
            word = s[startIndex:index]
            if(char in word):
                curLength = len(word)
                if(curLength > maxLength):
                    maxLength = curLength
                while(char in word and startIndex <= index):
                    startIndex += 1
                    word = s[startIndex:index]
            else:
                word = s[startIndex:index+1]
                curLength = len(word)
                if(curLength > maxLength):
                    maxLength = curLength
        return maxLength
