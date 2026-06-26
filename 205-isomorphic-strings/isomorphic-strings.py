class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        mapST = {}
        mapTS = {}

        for i in range(len(s)):

            ch1 = s[i]
            ch2 = t[i]

            if ch1 in mapST:

                if mapST[ch1] != ch2:
                    return False

            else:

                mapST[ch1] = ch2

            if ch2 in mapTS:

                if mapTS[ch2] != ch1:
                    return False

            else:

                mapTS[ch2] = ch1

        return True