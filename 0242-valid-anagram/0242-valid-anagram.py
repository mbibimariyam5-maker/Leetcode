class Solution(object):
    def isAnagram(self, s, t):
        s = sorted(s)
        t = sorted(t)
        if len(s) == len(t) and s == t:
            return True
        else:
            return False

        