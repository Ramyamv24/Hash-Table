from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        count = Counter(nums)

        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            bucket[freq].append(num)

        res = []

        for i in range(len(nums), 0, -1):
            for num in bucket[i]:
                res.append(num)

                if len(res) == k:
                    return res


# Main Part
nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
k = int(input("Enter k: "))

obj = Solution()
result = obj.topKFrequent(nums, k)

print("Top", k, "frequent elements:", result)