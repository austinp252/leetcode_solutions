class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # edge cases
        if((x < 0) or (x % 10 == 0 and x != 0)):  # negative or 0 in 1s place
            return False
        else:  # run checking algo
            revertedNum = 0
            while(x > revertedNum):  # loop that decrements x by powers of 10 to get each digit
                # adds last digit of x to end of revertedNum
                revertedNum = revertedNum * 10 + x % 10
                x /= 10
            return(x == revertedNum or x == revertedNum/10)
