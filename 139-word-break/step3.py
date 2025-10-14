class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # s[i:] がwordDictの単語群から生成できるか
        can_generate = [False] * (len(s) + 1)
        can_generate[-1] = True

        for i in reversed(range(len(s))):
            for word in wordDict:
                if len(s) < i + len(word):
                    continue
                if s[i : i + len(word)] == word:
                    can_generate[i] |= can_generate[i + len(word)]

        return can_generate[0]
