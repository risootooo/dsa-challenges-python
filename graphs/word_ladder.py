"""
Problem: Word Ladder
Given a begin word, an end word and a word list, return the number of
words in the shortest transformation sequence from begin to end, where
each step changes exactly one letter and every intermediate word must
be in the word list. Return 0 if no such sequence exists. The begin
word itself need not be in the list; the end word must be.
Example: begin="hit", end="cog",
wordList=["hot","dot","dog","lot","log","cog"] -> 5 ("hit"->"hot"->
"dot"->"dog"->"cog"); begin="hit", end="cog",
wordList=["hot","dot","dog","lot","log"] -> 0

Approach: Breadth-first search over words. Two words are neighbours
when they differ in exactly one position. To find neighbours without
an O(N^2 * L) all-pairs scan, each word is indexed under L wildcard
patterns (e.g. "hot" -> "*ot", "h*t", "ho*"), so all words sharing a
pattern are one-letter neighbours. BFS explores level by level, so
the first time the end word is reached its level is the shortest
sequence length. Visited words are removed from the pattern index so
each word is expanded at most once. The input list is never mutated.

Time Complexity: O(N * L^2) — N words, L patterns each, pattern
construction costs O(L) per word
Space Complexity: O(N * L) for the pattern index
"""

from __future__ import annotations

from collections import defaultdict, deque


def ladder_length(begin_word: str, end_word: str, word_list: list[str]) -> int:
    """Length of the shortest one-letter transformation, or 0 if none."""
    if not begin_word or not end_word or begin_word == end_word:
        return 0
    words = set(word_list)
    if end_word not in words:
        return 0
    words.add(begin_word)
    length = len(begin_word)
    patterns: dict[str, list[str]] = defaultdict(list)
    for word in words:
        if len(word) != length:
            continue
        for i in range(length):
            patterns[word[:i] + "*" + word[i + 1 :]].append(word)

    queue: deque[str] = deque([begin_word])
    visited: set[str] = {begin_word}
    steps = 1
    while queue:
        for _ in range(len(queue)):
            word = queue.popleft()
            if word == end_word:
                return steps
            for i in range(length):
                key = word[:i] + "*" + word[i + 1 :]
                for neighbour in patterns.get(key, []):
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)
                patterns[key] = []
        steps += 1
    return 0


if __name__ == "__main__":
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    assert ladder_length("hit", "cog", words) == 5
    assert words == ["hot", "dot", "dog", "lot", "log", "cog"]  # untouched
    assert ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0
    assert ladder_length("a", "c", ["a", "b", "c"]) == 2
    assert ladder_length("hit", "hit", ["hit"]) == 0
    assert ladder_length("", "cog", ["cog"]) == 0
    assert ladder_length("hit", "", ["hit"]) == 0
    assert ladder_length("hit", "cog", []) == 0
    print("word_ladder: OK")
