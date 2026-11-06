from collections import deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}
        indegree = {c: 0 for c in adj}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            for a, b in zip(w1, w2):
                if a != b:
                    if b not in adj[a]:
                        adj[a].add(b)
                        indegree[b] += 1
                    break

        q = deque(c for c in indegree if indegree[c] == 0)
        res = []

        while q:
            c = q.popleft()
            res.append(c)

            for nei in adj[c]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return "".join(res) if len(res) == len(indegree) else ""