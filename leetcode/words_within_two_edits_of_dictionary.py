# 2452. Words Within Two Edits of Dictionary
# https://leetcode.com/problems/words-within-two-edits-of-dictionary/


# Based on Editorial's Approach 2: Trie
class Solution:
    def twoEditWords(
        self, queries: list[str], dictionary: list[str]
    ) -> list[str]:
        # Build a trie over the dictionary; each node is a dict of char -> node.
        # An empty string key "" marks the end of a word.
        trie: dict = {}
        for w in dictionary:
            node = trie
            for c in w:
                node = node.setdefault(c, {})
            node[""] = True

        # DFS the trie allowing up to 2 mismatches with the query.
        def dfs(node: dict, i: int, q: str, edits: int) -> bool:
            if edits > 2:
                return False
            if i == len(q):
                return "" in node
            for c, child in node.items():
                if c == "":
                    continue
                if dfs(child, i + 1, q, edits + (c != q[i])):
                    return True
            return False

        return [q for q in queries if dfs(trie, 0, q, 0)]
