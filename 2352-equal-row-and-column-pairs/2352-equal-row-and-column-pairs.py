class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # tracking every row and every item put them to separate map and compare them
        length = len(grid)
        rows = {}
        columns = {}
        for i in range(length):
            temp = ''
            for j in range(length):
                temp += str(grid[i][j]) + str(j)
            rows[temp] = 1 + rows.get(temp,0)
        for i in range(length):
            temp = ''
            for j in range(length):
                temp += str(grid[j][i]) + str(j)
            columns[temp] = 1 + columns.get(temp,0)
        count = 0
        for key,value in rows.items():
            if key in columns:
                count += value * columns[key]
                
        return count