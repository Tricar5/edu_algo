"""

"""

import typing as tp


class Solution:
    def numIslands(self, grid: tp.List[tp.List[str]]) -> int:

        cnt = 0
        r, c = len(grid), len(grid[0])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j):
            for x, y in directions:

                dx, dy = i + x, j + y

                if 0 <= dx < r and 0 <= dy < c:

                    if grid[dx][dy] == '1':
                        grid[dx][dy] = 'X'
                        dfs(dx, dy)

        for i in range(0, r):
            for j in range(0, c):
                if grid[i][j] == '1':
                    dfs(i, j)
                    cnt += 1

        return cnt