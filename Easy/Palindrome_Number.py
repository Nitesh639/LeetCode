class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            number = str(x)
            ran = len(number)
            pal = ""
            for i in range(1, ran + 1):
                pal += number[-i]

            x2 = int(pal)
            return x == x2

# Given an integer x, return true if x is palindrome integer.
#
# An integer is a palindrome when it reads the same backward as forward.
#
# For example, 121 is a palindrome while 123 is not.

# Example 1:
#
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:
#
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
