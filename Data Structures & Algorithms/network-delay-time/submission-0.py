import heapq

class Solution:
    def networkDelayTime(self, times, n, k):
        graph = {i: [] for i in range(1, n + 1)}

        for u, v, w in times:
            graph[u].append((v, w))

        min_heap = [(0, k)]
        visited = set()
        result = 0

        while min_heap:
            time, node = heapq.heappop(min_heap)

            if node in visited:
                continue

            visited.add(node)
            result = time

            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (time + weight, neighbor))

        return result if len(visited) == n else -1