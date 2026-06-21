from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ans = []
        d = {word[::-1]: i for i, word in enumerate(words)}

        for i, word in enumerate(words):
            if "" in d and d[""] != i and word == word[::-1]:
                ans.append([i, d[""]])

            for j in range(1, len(word) + 1):
                l = word[:j]
                r = word[j:]

                if l in d and d[l] != i and r == r[::-1]:
                    ans.append([i, d[l]])

                if r in d and d[r] != i and l == l[::-1]:
                    ans.append([d[r], i])

        return ans


# Main Part
n = int(input("Enter number of words: "))

words = []
for i in range(n):
    word = input(f"Enter word {i+1}: ")
    words.append(word)

obj = Solution()
result = obj.palindromePairs(words)

print("Palindrome Pairs:")
print(result)