# 2130. Maximum Twin Sum of a Linked List
# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/


# Based on Editorial's Approach 3: Reverse Second Half In Place
class Solution:
    def pairSum(self, head) -> int:
        # Find the middle via slow/fast pointers.
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        # Reverse the second half in place.
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # Walk both halves and track the maximum twin sum.
        ans = 0
        node = head
        while prev:
            ans = max(ans, node.val + prev.val)
            node, prev = node.next, prev.next
        return ans
