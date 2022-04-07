class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Spread from center char

        # check left and right on current char until pair doesnt match
        # iterate each char (or pair)
        # check index - i chars and index + i chars to see if match
        # if they match, current SS = string[index-i:index+i]
        # fail check is that index is in bounds and the characters match
        # iterate again
        # at failure, check current SS against max SS

        # cond for even len SS, iterate starting from second char and include previous char
        # iterations are index[0]-i and index[1]+i
        # index[0] and index[1] must match

        maxSS = ''
        for index, char in enumerate(s):
            oddMaxSS = ''
            evenMaxSS = ''
            curMaxSS = ''
            # odd case
            oddCount = 0
            while(True):
                if((index-oddCount) >= 0 and (index+oddCount) < len(s)):
                    if(s[index-oddCount] == s[index+oddCount]):
                        oddMaxSS = s[index-oddCount:index+oddCount+1]
                        oddCount += 1
                    else:
                        break
                else:
                    break
            # even case
            evenCount = 0
            while(True):
                if(index-evenCount >= 0 and index+evenCount+1 < len(s)):
                    if(s[index-evenCount] == s[index+evenCount+1]):
                        evenMaxSS = s[index-evenCount:index+evenCount+2]
                        evenCount += 1
                    else:
                        break
                else:
                    break
            curMaxSS = (oddMaxSS if len(oddMaxSS) >=
                        len(evenMaxSS) else evenMaxSS)
            maxSS = (curMaxSS if len(curMaxSS) > len(maxSS) else maxSS)
        return maxSS
