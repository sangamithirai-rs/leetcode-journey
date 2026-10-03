# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1

        while left < right:

            # Skip spaces and punctuation from the left
            if not s[left].isalnum():
                left += 1
                continue

            # Skip spaces and punctuation from the right
            if not s[right].isalnum():
                right -= 1
                continue

            # Compare characters ignoring case
            if s[left].lower() != s[right].lower():
                return False

            # Move both pointers toward the center
            left += 1
            right -= 1

        return True
