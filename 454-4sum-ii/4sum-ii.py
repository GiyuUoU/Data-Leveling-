class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):

        freq = {}

        for a in nums1:
            for b in nums2:

                total = a + b
                freq[total] = freq.get(total, 0) + 1

        ans = 0

        for c in nums3:
            for d in nums4:

                target = -(c + d)

                if target in freq:
                    ans += freq[target]

        return ans