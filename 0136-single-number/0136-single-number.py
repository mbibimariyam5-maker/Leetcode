class Solution(object):
    def singleNumber(self, nums):
        hash = {}
        for i in range(len(nums)):
            if nums[i] in hash:
                hash[nums[i]] += 1
            else:
                hash[nums[i]] = 1

        for i in hash:
            if hash[i] == 1:
                return i
        