#并查集模板套用
#其实个人感觉中等题目无脑套用模板
#然后走遍for循环得到[祖先，祖先，祖先。。。]的p数组，然后再操作即可
def findCircleNum(arrs):
    if not arrs:
        return 0
    def union(p,i,j):
        p1= parent(p,i)
        p2 = parent(p,j)
        p[p1] = p2
    
    def parent(p,i):
        root = i
        while(root!=p[root]):
            root = p[root]
        while p[i]!=i:
            x = i
            i = p[i]
            p[x] = root
        return root
    
    p  = [i for i in range(len(arrs))]
    #套用并查集模板
    for i in range(len(arrs)):
        for j in range(i+1,len(arrs)):
            if arrs[i][j] ==1:
                union(p,i,j)
    #得到每个对应的最大祖先
    for i in range(len(arrs)):
        parent(p,i)
    return len(set(p))
    
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
print(findCircleNum(isConnected))