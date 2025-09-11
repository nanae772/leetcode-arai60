from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        group_anagrams: dict[str, list[str]] = defaultdict(list)
        for s in strs:
            sorted_string = "".join(sorted(s))
            group_anagrams[sorted_string].append(s)
        return list(group_anagrams.values())
