from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        c = {}

        for i in nums:
            c[i] = c.get(i, 0) + 1

        l = []

        for k, v in c.items():
            if v == 2:
                l.append(k)

        return l


if __name__ == "__main__":
    n = int(input("Enter number of elements: "))

    nums = []
    print("Enter elements:")
    for i in range(n):
        nums.append(int(input()))

    sol = Solution()
    result = sol.findDuplicates(nums)

    print("Duplicate elements:", result)