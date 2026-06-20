# Problem: palindrome number
# Difficulty: easy
# Approach:
#convert the number to string
#reverse the string
#compare both original and reversed string

# time complexity: O(n)
# space complexity: O(n)


class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]