from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top_k_frequent = Counter(nums).most_common(k)
        return [value for value, _ in top_k_frequent]
