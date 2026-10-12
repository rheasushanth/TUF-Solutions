class Solution:
    def twoSum(self, nums, target):
        freq = {}
        for i in range(len(nums)):
            if (target - nums[i]) in freq:
                return [i,freq[target - nums[i]]]
            else:
                freq[nums[i]] = i
     


        