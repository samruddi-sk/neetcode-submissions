class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []

        def dfs(start, path, total):
            if total == target:
                res.append(path[:])
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if total + candidates[i] > target:
                    break

                dfs(i + 1, path + [candidates[i]], total + candidates[i])

        dfs(0, [], 0)
        return res