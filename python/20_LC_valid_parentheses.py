class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # stack FILO
        stack = []
        for char in s:
            # check for closing
            if(char == ']' or char == ')' or char == '}'):
                if(len(stack) == 0):
                    return False
                opening = stack.pop(0)
                if(char == ')' and not opening == '('):
                    return False
                elif(char == ']' and not opening == '['):
                    return False
                elif(char == '}' and not opening == '{'):
                    return False
            else:
                stack.insert(0, char)
        return True if len(stack) == 0 else False
