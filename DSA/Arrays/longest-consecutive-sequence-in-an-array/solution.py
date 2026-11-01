class Solution:
    def longestConsecutive(self, nums):
        numsset = set(nums)
        longest = 0
        for num in numsset:
            if num - 1 not in numsset:
                count = 1
                curr = num
                while curr + 1 in numsset:
                    count+=1
                    curr+=1
                longest = max(longest, count)
        return longest


