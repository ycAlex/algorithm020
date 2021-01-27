#动态规划，当前位置的最小路劲值，取决于他的上方或者左侧的最小值再加上当前值

def minPathsum(grid):
    #先处理边界，第一行和第一列
    for i in range(1,len(grid)):
        grid[0][i] +=grid[0][i-1]
    
    for i in range(1,len(grid[0])):
        grid[i][0] +=grid[i-1][0]
    #然后每次更新从左侧或者上方过来的最小值
    for i in range(1,len(grid)):
        for j in range(1,len(grid[0])):
            grid[i][j] += min(grid[i-1][j],grid[i][j-1])

    return grid[-1][-1]

grid = [[1,3,1],[1,5,1],[4,2,1]]

print(minPathsum(grid))