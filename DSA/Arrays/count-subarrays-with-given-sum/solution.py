class Solution:
    def subarraySum(self, nums, k):
        prefix_sum = {0: 1}
        total = 0
        count = 0

        for num in nums:
            total += num

            target = total - k

            if target in prefix_sum:
                count += prefix_sum[target]

            if total not in prefix_sum:
                prefix_sum[total] = 0

            prefix_sum[total] += 1

        return count