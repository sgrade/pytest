# 3093. Longest Common Suffix Queries
# https://leetcode.com/problems/longest-common-suffix-queries/


# Based on Editorial's Approach: Trie
class TrieNode:
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.min_len = float("inf")
        self.idx = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Insert reversed word; track shortest word's index at every prefix node.
    def insert(self, s: str, idx: int) -> None:
        def update(node: TrieNode) -> None:
            if len(s) < node.min_len:
                node.min_len = len(s)
                node.idx = idx

        node = self.root
        update(node)
        for ch in s:
            node = node.children.setdefault(ch, TrieNode())
            update(node)

    # Walk down as far as the reversed query matches; return best index seen.
    def query(self, s: str) -> int:
        node = self.root
        for ch in s:
            if ch not in node.children:
                break
            node = node.children[ch]
        return node.idx


class Solution:
    def stringIndices(
        self, wordsContainer: list[str], wordsQuery: list[str]
    ) -> list[int]:
        # Reverse strings so suffix matching becomes prefix matching in a trie.
        trie = Trie()
        for i, word in enumerate(wordsContainer):
            trie.insert(word[::-1], i)
        return [trie.query(q[::-1]) for q in wordsQuery]
