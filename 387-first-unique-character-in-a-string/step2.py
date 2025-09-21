from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_to_count = Counter(s)
        for i, ch in enumerate(s):
            if char_to_count[ch] == 1:
                return i
        return -1
