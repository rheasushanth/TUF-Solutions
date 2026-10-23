class Solution:
    def threeSum(self, nums: list) -> list[list]:
        nums.sort()
        n = len(nums)
        s = set()
        for i in range(n-2):
            left, right = i+1, n-1
            while left<right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    s.add((nums[i],nums[left],nums[right]))
                    left+=1
                    right-=1
                elif total < 0:
                    left+=1
                else:
                    right-=1
        return [list(k) for k in s]
        