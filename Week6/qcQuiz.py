def qcQuiz(n,steps):
    if n ==1 or n==2:
        return n
    
    dp = [[] for _ in range(n+1)]
    
    dp[0].append('0')
    dp[1].append('1')
    dp[2].append('2')
    
    for i in range(3,n+1):
        for each in steps:
            if i - each >=0:
                tmp = dp[i-each]
                for e2 in tmp:
                    if e2[-1]!=str(each):
                        dp[i].append(e2+str(each))
       
        
    print(dp[5])
    print(len(dp[5]))
    return len(dp[-1])
 
res = qcQuiz(10,[1,2,3])
print(res)