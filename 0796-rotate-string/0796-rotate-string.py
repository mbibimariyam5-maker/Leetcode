class Solution(object):
    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False

        for i in range(len(s)):
            if s == goal:
                return True

            s = s[1:] + s[0]

        return False
        