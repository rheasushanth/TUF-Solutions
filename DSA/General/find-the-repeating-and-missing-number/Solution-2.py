class Solution:
    def findMissingRepeatingNumbers(self, nums):
        freq = {}
        k = []
        n = len(nums)
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        for r in freq:
            if freq[r] > 1:
                k.append(r)
        for i in range(1,n+1):
            if i not in freq:
                k.append(i)
        return k
            
            