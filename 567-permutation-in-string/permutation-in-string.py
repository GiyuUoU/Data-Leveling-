class Solution:
    def checkInclusion(self, s1, s2):

        k = len(s1)

        target = sorted(s1)

        for i in range(len(s2) - k + 1):

            if sorted(s2[i:i+k]) == target:
                return True

        return False