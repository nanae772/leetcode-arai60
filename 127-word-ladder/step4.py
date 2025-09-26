class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0

        word_list = [beginWord] + wordList
        adjacent_graph = self._build_adjacent_graph(word_list)
        node_and_distances = deque([(0, 1)])
        is_visited = [False] * len(word_list)
        goal = word_list.index(endWord)

        while node_and_distances:
            node, distance = node_and_distances.popleft()
            if node == goal:
                return distance

            for next_node in adjacent_graph[node]:
                if is_visited[next_node]:
                    continue
                node_and_distances.append((next_node, distance + 1))
                is_visited[next_node] = True

        return 0

    def _build_adjacent_graph(self, word_list: list[str]) -> list[list[int]]:
        def is_one_letter_diff(s: str, t: str) -> int:
            count_diff = 0
            for ch_s, ch_t in zip(s, t):
                if ch_s != ch_t:
                    count_diff += 1
                if count_diff > 1:
                    return False
            return count_diff == 1

        adjacent_graph = [[] for _ in range(len(word_list))]
        for i in range(len(word_list)):
            for j in range(i + 1, len(word_list)):
                if not is_one_letter_diff(word_list[i], word_list[j]):
                    continue
                adjacent_graph[i].append(j)
                adjacent_graph[j].append(i)

        return adjacent_graph
