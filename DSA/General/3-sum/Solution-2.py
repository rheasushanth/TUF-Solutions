class Solution:
    def threeSum(self, nums: list) -> list[list]:
        nums.sort()
        n = len(nums)
        l = []
        for i in range(n-2):
            left, right = i+1, n-1
            if i>0 and nums[i] == nums[i-1]:
                continue
            while left<right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    l.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left < right and nums[left] == nums[left-1]:
                        left+=1
                    while left < right and nums[right] == nums[right+1]:
                        right-=1
                elif total< 0:
                    left+=1
                else:
                    right-=1
                
        return l
        