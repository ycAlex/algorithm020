#动态规划-股票买卖一次

#二维解决股票买卖问题
#每一天有两种情况，持有或者不持有，也就是买或者卖

def maxProfit(arrs):
    if len(arrs)<2:
        return 0
    #初始化dp数组
    #第一天对应两种情况，0代表了没持有，1代表了持有
    dp = [[0,0]]
    #第一天持有，买入股票则[0][1]=-arrs[0]
    dp[0][1] = -arrs[0]
    
    for i in range(1,len(arrs)):
        dp.append([0,0])
        #到第i天没有持有股票的最大值，要么是前一天就没有，要么是前一天有，我卖掉
        dp[i][0] = max(dp[i-1][0], dp[i-1][1]+arrs[i])
        #第i天持有股票的最大值，要么是我前一天持有，或者是当天持有
        dp[i][1] = max(dp[i-1][1],-arrs[i])
    return dp[-1][0]
    
#降维处理
#因为这里其实我们需要用到的就是前面所走过的最小值，最小值然后结合当天的钱数看能否得到最大利润
#也就是说其实只需要更新两个值：最大卖出利润和最小买入价钱
def maxProfit2(arrs):
    if len(arrs)<2:
        return 0
    buy = arrs[0]
    sell = 0
    
    for i in range(1,len(arrs)):
        #每次更新Buy到小的，同时更新sell到最大的
        buy = min(buy,arrs[i])
        sell = max(sell, arrs[i] - buy)
    return sell 

a = [7,1,5,3,6,4]
print(maxProfit(a))
print(maxProfit2(a))
    

    
