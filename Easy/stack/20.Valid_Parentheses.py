class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        data = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c not in data:
                stack.append(c)  # if c is not belongs to close parentheses than add it
                continue  # and go to next element

            if not stack or stack[-1] != data[c]:  # if stack have element or last element of stack is not
                return False  # belongs to value of data[c] if and one true it's return false
            stack.pop()
        return not stack  # if stack is empty return true

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is
# valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# Example 1:
#
# Input: s = "()"
# Output: true
# Example 2:
#
# Input: s = "()[]{}"
# Output: true
# Example 3:
#
# Input: s = "(]"
# Output: false
