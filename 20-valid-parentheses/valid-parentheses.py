class Solution(object):
    def isValid(self, s):

        stack = []
        mapping = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        for i in s:

            if i in "([{":
                stack.append(i)

            else:

                if not stack:
                    return False

                top = stack.pop()

                if top != mapping[i]:
                    return False

        return len(stack) == 0
        """
        :type s: str
        :rtype: bool
        """
        