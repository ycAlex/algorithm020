#升维处理一下
#定义两个维度-偷或者不偷
def rob(arrs):
    dp= [[0,0]]
    for i in range(len(arrs)):
        dp.append([0,0])
        #如果到这天我偷了，则是当前天的数目+前一天没偷的结果
        dp[i+1][0] = dp[i][1]+nums[i]
        #如果当前天我没偷，则看前一天，偷或者不偷的最大值即可
        dp[i+1][1] = max(dp[i][0],dp[i][1])
    
    return max(dp[-1])
