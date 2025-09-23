class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0

        word_list = [beginWord] + wordList[:]

        def count_different_characters(s: str, t: str) -> int:
            count = 0
            for ch_s, ch_t in zip(s, t):
                if ch_s != ch_t:
                    count += 1
            return count

        adjacent_graph = [[] for _ in range(len(word_list))]
        for i in range(len(word_list)):
            for j in range(i + 1, len(word_list)):
                if count_different_characters(word_list[i], word_list[j]) != 1:
                    continue
                adjacent_graph[i].append(j)
                adjacent_graph[j].append(i)

        distance = [None] * len(word_list)
        distance[0] = 1
        nodes = deque()
        nodes.append(0)

        while nodes:
            node = nodes.popleft()
            for next_node in adjacent_graph[node]:
                if distance[next_node] is not None:
                    continue
                distance[next_node] = distance[node] + 1
                nodes.append(next_node)

        goal_index = word_list.index(endWord)
        if distance[goal_index] is None:
            return 0
        return distance[goal_index]
