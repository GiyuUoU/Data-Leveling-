class Solution:
    def findAnagrams(self, s: str, p: str):

        ans = []

        target = sorted(p)
        k = len(p)

        for i in range(len(s) - k + 1):

            if sorted(s[i:i+k]) == target:
                ans.append(i)

        return ans