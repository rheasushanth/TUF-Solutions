class Solution:
    def powerSet(self, nums):
        #your code goes here
        result = []
        subset = []

        def backtrack(index):
            if len(nums) == index:
                result.append(subset.copy())
                return
            
            subset.append(nums[index])
            backtrack(index + 1)

            subset.pop()

            backtrack(index + 1)
        backtrack(0)
        return result