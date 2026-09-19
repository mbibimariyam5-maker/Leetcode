class Solution:
    def subarraySum(self, nums, k):
        count = 0
        total = 0
        hash = {0: 1}

        for num in nums:
            total += num

            if total - k in hash:
                count += hash[total - k]

            hash[total] = hash.get(total, 0) + 1

        return count