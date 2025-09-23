from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top_k_frequent = [value for value, _ in Counter(nums).most_common(k)]
        return top_k_frequent
