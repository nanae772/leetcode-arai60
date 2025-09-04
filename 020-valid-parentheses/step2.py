class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = []
        open_to_close = {"(": ")", "[": "]", "{": "}"}
        for bracket in s:
            if bracket in open_to_close:
                open_brackets.append(bracket)
                continue
            if not open_brackets or bracket != open_to_close[open_brackets.pop()]:
                return False
        return not open_brackets
