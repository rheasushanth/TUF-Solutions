class Solution:
    def majorityElement(self, nums):
        freq = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in freq:
                freq[nums[i]] +=1
            else:
                freq[nums[i]] = 1
            if freq[nums[i]] > n/2:
                return nums[i]
        