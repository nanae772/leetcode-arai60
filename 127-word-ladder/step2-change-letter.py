class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        def generate_one_letter_variants(word: str) -> str:
            """wordの各文字をa-zの各文字に置き換えた文字列を列挙する"""
            for i in range(len(word)):
                for letter in ascii_lowercase:
                    yield word[:i] + letter + word[i + 1 :]

        nodes = deque()
        nodes.append((beginWord, 1))
        available_words = set(wordList)
        seen_words = {beginWord}

        while nodes:
            word, distance = nodes.popleft()
            if word == endWord:
                return distance

            for new_word in generate_one_letter_variants(word):
                if new_word not in available_words or new_word in seen_words:
                    continue
                nodes.append((new_word, distance + 1))
                seen_words.add(new_word)

        return 0
