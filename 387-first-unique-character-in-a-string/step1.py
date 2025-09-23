class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_to_index_and_count = dict()
        for i, ch in enumerate(s):
            if ch not in char_to_index_and_count:
                char_to_index_and_count[ch] = (i, 1)
            else:
                index, count = char_to_index_and_count[ch]
                char_to_index_and_count[ch] = (index, count + 1)
        first_unique_char_index = min(
            (index for index, count in char_to_index_and_count.values() if count == 1),
            default=-1,
        )
        return first_unique_char_index
