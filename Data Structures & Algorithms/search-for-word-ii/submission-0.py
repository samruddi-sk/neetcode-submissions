class Solution:
    def findWords(self, board, words):
        root = {}
        for word in words:
            node = root
            for ch in word:
                node = node.setdefault(ch, {})
            node["$"] = word

        res = []
        R, C = len(board), len(board[0])

        def dfs(r, c, node):
            ch = board[r][c]
            if ch not in node:
                return

            node = node[ch]
            if "$" in node:
                res.append(node.pop("$"))

            board[r][c] = "#"
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and board[nr][nc] != "#":
                    dfs(nr, nc, node)
            board[r][c] = ch

        for r in range(R):
            for c in range(C):
                dfs(r, c, root)

        return res