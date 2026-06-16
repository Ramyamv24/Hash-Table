from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        c = Counter(nums)
        l = []

        for k, v in c.items():
            if v > n / 3:
                l.append(k)

        return l


# Main Part
nums = list(map(int, input("Enter numbers separated by space: ").split()))

obj = Solution()
result = obj.majorityElement(nums)

print("Majority elements:", result)