import sys

sys.setrecursionlimit(10**4)

# 再帰下降構文解析(Recursive Descent Parsing)による解法


class Solution:
    def isValid(self, s: str) -> bool:
        """(),[],{}からなる文字列sの整合性が取れているか判定する"""
        return BrancketsStringValidator(s).is_valid()


class BrancketsStringValidator:
    """再帰下降構文解析を用いたパーサー"""

    def __init__(self, s: str) -> None:
        self.s = s
        self.i = 0

    def is_valid(self) -> bool:
        """(),[],{}からなる文字列sの整合性が取れているか判定する"""
        return self._can_parse() and self.i == len(self.s)

    def _peek(self) -> str | None:
        if self.i >= len(self.s):
            return None
        return self.s[self.i]

    def _consume(self, ch: str) -> bool:
        if self._peek() != ch:
            return False
        self.i += 1
        return True

    def _can_parse(self) -> bool:
        """文字列s[i:]をパースできるか判定する

        実装は以下の文法に基づく
        S -> '(' S ')' | '[' S ']' | '{' S '}' | (空文字)
        """
        open_to_close = {"(": ")", "{": "}", "[": "]"}
        if self._peek() not in open_to_close:
            return True

        open_bracket = self._peek()
        close_bracket = open_to_close[open_bracket]
        if (
            not self._consume(open_bracket)
            or not self._can_parse()
            or not self._consume(close_bracket)
        ):
            return False
        return self._can_parse()
