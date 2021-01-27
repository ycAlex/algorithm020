def leastInterval(arrs):
    if not arrs:
        return 0
        
    tmp = collections.Counter(arrs)
    tmost = tmp.most_common()
    fre_most,cnt = tmost[0][1],1
    for i in range(1,len(tmost)):
        if most[i][1] == fre_most:
            cnt+=1
    
    res = (fre_most-1)*(n+1)+cnt
    if res<len(arrs):
        return res 
 
arrs = ["A","A","A","B","B","B"]