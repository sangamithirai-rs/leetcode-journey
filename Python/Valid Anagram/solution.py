# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def isAnagram(self, s, t):
        count = {}

        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        for char in t:
            if char not in count:
                return False

            count[char] -= 1

        for value in count.values():
            if value != 0:
                return False

        return True
