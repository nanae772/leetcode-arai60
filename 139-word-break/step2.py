class SolutionRollingHash:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        MOD = 10**9 + 7  # 十分大きな素数
        BASE = 29  # MODと互いに素なら何でもよい？

        def get_index_letter(ch: str) -> int:
            # a, aa, aaa... が同じにならないよう
            # a -> 1, b -> 2, ..., z -> 26 と対応付ける
            return ord(ch) - ord("a") + 1

        def calculate_next_hash(hash_: int, ch: str) -> int:
            return (hash_ * BASE + get_index_letter(ch)) % MOD

        word_hashes = set()
        prefix_hashes = set()
        for word in wordDict:
            hash_ = 0
            for ch in word:
                hash_ = calculate_next_hash(hash_, ch)
                prefix_hashes.add(hash_)
            word_hashes.add(hash_)

        can_generate = [False] * (len(s) + 1)
        can_generate[-1] = True

        for left in reversed(range(len(s))):
            hash_ = 0
            right = left
            while right < len(s):
                hash_ = calculate_next_hash(hash_, s[right])
                right += 1
                if hash_ not in prefix_hashes:
                    break
                if hash_ in word_hashes:
                    can_generate[left] |= can_generate[right]

        return can_generate[0]
