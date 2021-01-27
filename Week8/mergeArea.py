#先排序，按照每个元素第一位进行排序
#每次比较下一个和前一个（可能是合并，也可能没合并）是否重合即可

def mergeArea(arrs):
    if not arrs:
        return []
    res = []
    #排序区间
    arrs.sort(key = lambda x:x[1])
    res.append(arrs[0])
    for i in range(1,len(arrs)):
        #通过和res的最后一个比较来查看是否需要合并
        if arrs[i][0]<=res[-1][1]:
            res[-1][1] = max(res[-1][1],arrs[i][1])
        else:
            res.append(arrs[i])
    return res 




intervals = [[1,3],[2,6],[8,10],[15,18]]

print(mergeArea(intervals))
