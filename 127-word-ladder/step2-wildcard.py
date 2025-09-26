class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        def generate_patterns_from_word(word: str) -> tuple[str, str]:
            """wordの一文字をワイルドカードにしたパターンをtupleとして列挙する

            例: "hot" -> ("","ot"), ("h","t"), ("ho","")
            """
            for i in range(len(word)):
                yield (word[:i], word[i + 1 :])

        def enumerate_adjacent_words(word: str) -> str:
            """wordから1文字だけ変えて出来るwordListに含まれる文字列を列挙する"""
            for pattern in generate_patterns_from_word(word):
                yield from pattern_to_words[pattern]

        pattern_to_words = defaultdict(list)
        for pattern in generate_patterns_from_word(beginWord):
            pattern_to_words[pattern].append(beginWord)
        for word in wordList:
            for pattern in generate_patterns_from_word(word):
                pattern_to_words[pattern].append(word)

        nodes = deque([(beginWord, 1)])
        seen_words = set()
        while nodes:
            word, distance = nodes.popleft()
            if word == endWord:
                return distance

            for adjacent_word in enumerate_adjacent_words(word):
                if adjacent_word in seen_words:
                    continue
                nodes.append((adjacent_word, distance + 1))
                seen_words.add(adjacent_word)

        return 0
