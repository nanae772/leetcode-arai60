from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        sorted_to_originals = defaultdict(list)
        for s in strs:
            sorted_string = "".join(sorted(s))
            sorted_to_originals[sorted_string].append(s)
        return list(sorted_to_originals.values())
