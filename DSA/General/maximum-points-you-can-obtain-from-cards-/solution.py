class Solution:
    def maxScore(self, cardScore, k):
        left_sum = 0

        for i in range(k):
            left_sum += cardScore[i]

        max_sum = left_sum
        right_sum = 0

        for i in range(k - 1, -1, -1):
            left_sum -= cardScore[i]
            right_sum += cardScore[len(cardScore) - (k - i)]

            max_sum = max(max_sum, left_sum + right_sum)

        return max_sum