class Solution(object):
    def rearrangeArray(self, nums):
        p = 0
        n = 1
        ans=[0]*len(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                ans[p] = nums[i]
                p += 2
            else:
                ans[n] = nums[i]
                n += 2

        return ans

        
        