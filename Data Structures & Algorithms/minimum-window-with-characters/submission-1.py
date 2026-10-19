class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        if len(t) > len(s):
            return ""

        need = Counter(t)
        window = {}
        have = 0
        required = len(need)
        left = 0
        min_length = float("inf")
        result = ""

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                have += 1

            while have == required:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    result = s[left:right + 1]

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1

        return result