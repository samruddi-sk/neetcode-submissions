from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        ROWS = len(grid)
        COLS = len(grid[0])

        queue = deque()

        # Step 1: Add all treasure chests to the queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))

        # Four possible directions
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        # Step 2: BFS
        while queue:

            r, c = queue.popleft()

            # Visit all four neighbors
            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                # Check boundaries
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                    continue

                # Only visit empty rooms
                if grid[nr][nc] != 2147483647:
                    continue

                # Set distance
                grid[nr][nc] = grid[r][c] + 1

                # Add the room to the queue
                queue.append((nr, nc))