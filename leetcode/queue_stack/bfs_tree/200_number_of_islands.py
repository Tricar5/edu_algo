from collections import deque
from typing import List
"""
class Solution(object):

    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        visited = set()
        islands = 0

        def bfs(r, c):

            q = deque()
            visited.add((r, c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                directions = [[1,0],[-1, 0], [0,1], [0, -1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and
                        c  in range(cols) and
                        grid[r][c] == '1' and
                        (r, c) not in visited):
                        q.append((r, c))
                        visited.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands

"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        count = 0

        if len(grid) == 1 and len(grid[0]) == 0:
            return count

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    count = count + 1
                    self.dfs(i, j, grid)
        return count

    def dfs(self, x, y, grid):

        if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[x]):
            if grid[x][y] == "1":
                grid[x][y] = "0"

                self.dfs(x - 1, y, grid)

                self.dfs(x + 1, y, grid)

                self.dfs(x, y - 1, grid)

                self.dfs(x, y + 1, grid)

grd = [["0", "1", "1"],
       ["1", "0", "0"],
       ["1", "0", "1"]]

c = Solution()

c.numIslands(grd)