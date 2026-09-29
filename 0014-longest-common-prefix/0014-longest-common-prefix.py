class Solution(object):
    def longestCommonPrefix(self, strs):
        ans = ""

        for j in range(len(strs[0])):
            for i in range(1, len(strs)):
                if j >= len(strs[i]) or strs[0][j] != strs[i][j]:
                    return ans

            ans += strs[0][j]

        return ans