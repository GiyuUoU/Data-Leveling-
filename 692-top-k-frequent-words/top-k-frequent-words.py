from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        freq = Counter(words)

        arr = sorted(freq.keys(), key=lambda word: (-freq[word], word))

        return arr[:k]