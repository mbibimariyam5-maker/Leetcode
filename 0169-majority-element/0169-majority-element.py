class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = {}
        max = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] in hash:
                hash[nums[i]] += 1
            else:
                hash[nums[i]] = 1

        for i in hash:
            if hash[i] > max:
                max = hash[i]
                ans = i
        return ans

        