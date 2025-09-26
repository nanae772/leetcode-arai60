class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0

        def generate_patterns_from_word(word: str) -> tuple[str, str]:
            for i in range(len(word)):
                yield (word[:i], word[i + 1 :])

        pattern_to_words = defaultdict(list)
        for pattern in generate_patterns_from_word(beginWord):
            pattern_to_words[pattern].append(beginWord)
        for word in wordList:
            for pattern in generate_patterns_from_word(word):
                pattern_to_words[pattern].append(word)

        def enumerate_adjacent_word(word: str) -> str:
            for pattern in generate_patterns_from_word(word):
                yield from pattern_to_words[pattern]

        nodes = deque([(beginWord, 1)])
        seen_words = {beginWord}
        while nodes:
            word, distance = nodes.popleft()
            if word == endWord:
                return distance

            for adjacent_word in enumerate_adjacent_word(word):
                if adjacent_word in seen_words:
                    continue
                nodes.append((adjacent_word, distance + 1))
                seen_words.add(adjacent_word)

        return 0
