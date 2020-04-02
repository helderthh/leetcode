# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/


class Solution:
    def __init__(self):
        self.visited = []
        self.count = 0
    
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        self.visited = []
        self.count = 0
        
        height = len(grid)
        width = len(grid[0])
        for _ in grid:
            self.visited.append([0] * width)
        
        for i in range(height):
            for j in range(width):
                # if visited or water
                if self.is_visited(i, j) or grid[i][j] == "0":
                    continue
                
                self.traverse(grid, i, j)

        return self.count

    def traverse(self, grid, i, j):
        if i < 0 or i >= len(grid):
            return
        if j < 0 or j >= len(grid[i]):
            return

        # if visited or water
        if self.is_visited(i, j) or grid[i][j] == "0":
            return
        # as not visited yet and is new land, mark it
        self.set_name(grid, i, j)

        self.traverse(grid, i, j + 1) # right
        self.traverse(grid, i - 1, j) # bottom
        self.traverse(grid, i, j - 1) # left
        self.traverse(grid, i + 1, j) # top

    def set_name(self, grid, i, j):        
        # check if there is land nearby already marked
        positions = [
            (i, j - 1),  # left
            (i - 1, j),  # top
            (i + 1, j),  # bottom
            (i, j + 1),  # right
        ]
        for next_i, next_j in positions:
            name = self.get_name(grid, next_i, next_j)
            # if a near land has name, use it
            if name:
                self.visited[i][j] = name
                return
    
        self.count += 1
        self.visited[i][j] = self.count
    
    def get_name(self, grid, i, j):
        if i < 0 or i >= len(grid):
            return None
        if j < 0 or j >= len(grid[i]):
            return None
        if grid[i][j] == "0":
            return None
        
        return self.visited[i][j]
    
    def is_visited(self, i, j):
        return self.visited[i][j] != 0
        
    
