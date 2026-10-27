class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(start, path):
            if start == len(s):
                res.append(path[:])
                return

            for end in range(start, len(s)):
                sub = s[start:end+1]

                if sub == sub[::-1]:
                    dfs(end+1, path + [sub])

        dfs(0, [])
        return res