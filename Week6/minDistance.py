#动规，升维的典型例子
#两个字符串构建二维数组，行，列分别代表了当前长度互相变为对方所需要的次数
#动态方程：具体看代码
def minDistance(s1,s2):
    #初始化长度分别加1，代表了双方都是从空字符串开始
    dp = [[10000 for i in range(len(s1)+1)] for _ in range(len(s2)+1)]
    #分别初始化第一行和第一列，也就是双方分别是空字符串变为对方的次数
    for i in range(len(s2)+1):
        dp[i][0] = i
    for i in range(len(s1)+1):
        dp[0][i] = i
    #双方分别从1开始代表了双方都有一个字符串开始变
    for i in range(1,len(s2)+1):
        for j in range(1,len(s1)+1):
            #如果当前的字符一样，则对角线过来的长度
            if s1[j-1] ==s2[i-1]:
                dp[i][j] = dp[i-1][j-1]
            #如果不一样，则选择上方，左侧，或者是对角线过来的那个最小值
            #也就是前面都一样，上方，左侧分别表示不一样
            else:
                dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
    print(dp)
    return dp[-1][-1]
                
     
    
    

word1 = "horse" 
word2 = "ros"

minDistance(word1,word2)