import functools


class SolutionWithMemoizeRecursion:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        @functools.cache
        def can_generate(i: int) -> bool:
            """s[i:]がwordDictの単語で生成できるか判定する"""
            if i == len(s):
                return True

            result = False
            for word in wordDict:
                if s[i : i + len(word)] == word:
                    result = result or can_generate(i + len(word))

            return result

        return can_generate(0)


class SolutionWithDP:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        can_generate = [False] * (len(s) + 1)
        can_generate[len(s)] = True

        for i in reversed(range(len(s))):
            for word in wordDict:
                if i + len(word) > len(s):
                    continue
                if s[i : i + len(word)] != word:
                    continue
                can_generate[i] |= can_generate[i + len(word)]

        return can_generate[0]
