#动规，如何得到最大边即可
#首先dp方程比原有的矩阵长宽各加1
#然后最大的边就是左侧和上方过来的最小值+1，因为上一步把长宽个扩了1，所以对于在边缘的‘1’永远是1

def maximalSquare(matrix):
    if not matrix:
        return 0
    
    dp = [[0 for _ in range(len(matrix[0])+1)] for _  in range(len(matrix)+1)]
    maxLength = 0
    #遍历矩阵
    for i in range(1,len(dp)):
        for j in range(1,len(dp[0])):
            #如果是‘1’更新最大长度
            if matrix[i-1][j-1] =='1':
                dp[i][j] = min(dp[i-1][j],dp[i][j-1])+1
                maxLength = max(dp[i][j],maxLength)
    
    return maxLength*maxLength
    
a = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(maximalSquare(a))


