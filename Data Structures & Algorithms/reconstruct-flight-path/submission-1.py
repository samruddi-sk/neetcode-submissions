class Solution:
    def findItinerary(self, tickets):
        graph = {}

        for start, end in sorted(tickets, reverse=True):
            graph.setdefault(start, []).append(end)


        result = []

        def dfs(airport):
            while airport in graph and graph[airport]:
                next_airport = graph[airport].pop()
                dfs(next_airport)

            result.append(airport)

        dfs("JFK")

        return result[::-1]