class Solution(object):
    def subarraySum(self, nums, k):

        count = 0
        sums = 0
        d = dict()
        d[0] = 1

        for i in range(len(nums)):
            sums += nums[i]
            count += d.get(sums - k, 0)
            d[sums] = d.get(sums, 0) + 1

        return count


# Main Part
nums = list(map(int, input("Enter array elements separated by space: ").split()))
k = int(input("Enter k: "))

obj = Solution()
result = obj.subarraySum(nums, k)

print("Number of subarrays with sum", k, "=", result)