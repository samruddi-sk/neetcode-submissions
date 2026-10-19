class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        from collections import Counter

        s1_count = Counter(s1)
        window_count = Counter(s2[:len(s1)])

        if s1_count == window_count:
            return True

        for right in range(len(s1), len(s2)):
            window_count[s2[right]] += 1

            left_char = s2[right - len(s1)]
            window_count[left_char] -= 1

            if window_count[left_char] == 0:
                del window_count[left_char]

            if s1_count == window_count:
                return True

        return False