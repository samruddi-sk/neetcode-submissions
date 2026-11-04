class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        visited = set()
        minDist = [float('inf')] * n
        minDist[0] = 0
        result = 0

        for _ in range(n):
            curr = -1

            for i in range(n):
                if i not in visited and (curr == -1 or minDist[i] < minDist[curr]):
                    curr = i

            visited.add(curr)
            result += minDist[curr]

            x1, y1 = points[curr]

            for i in range(n):
                if i not in visited:
                    x2, y2 = points[i]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    minDist[i] = min(minDist[i], dist)

        return result