class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = ["", "", "abc", "def", "ghi", "jkl",
                 "mno", "pqrs", "tuv", "wxyz"]
        res = []

        def backtrack(i, path):
            if i == len(digits):
                res.append(path)
                return

            for ch in phone[int(digits[i])]:
                backtrack(i + 1, path + ch)

        backtrack(0, "")
        return res