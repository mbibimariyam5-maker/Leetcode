class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        s = "".join(ch for ch in s if ch.isalnum())
        st = s[::-1]
        if s == st:
            return True
        else:
            return False
        