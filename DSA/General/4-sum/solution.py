class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        num = set()
        n = len(nums)
        for i in range(len(nums)-3):
            for j in range(i+1, n-2):
                left, right = j+1,n-1
                while left < right:
                    total = nums[i] + nums[left] + nums[right] + nums[j]
                    if total == target:
                        num.add((nums[i],nums[j],nums[left],nums[right]))
                        left+=1
                        right-=1
                    elif total < target:
                        left+=1
                    else:
                        right-=1
        return [list(k) for k in num]


            

        