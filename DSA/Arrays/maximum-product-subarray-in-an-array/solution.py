class Solution:
    def maxProduct(self, nums):
        maxProduct = minProduct = result = nums[0]
        for num in nums[1:]:
            if num<0:
                maxProduct, minProduct = minProduct, maxProduct
            maxProduct = max(num, maxProduct*num)
            minProduct = min(num, minProduct*num)

            result = max(result, maxProduct)
        return result
