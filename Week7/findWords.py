#关键是两点:
#借助tire树来检索Words-因为根据题意，在board里面可能不是顺序形成word-下下下这种，可能是上，有，下这种连在一起
#如何快速dfs，完成剪枝-通过标记然后复位
def findWords(arrs, words):
    tire = {}
    #构建一个tire树
    for each in words:
        t = tire
        for w in each:
            t = t.setdefault(w,{})
        t['#'] = 0
    
    res = []
    #深度搜索
    def dfs(i,j,tire,s):
        cur = arrs[i][j]
        #如果不在树中直接返回
        if cur not in tire:
            return 
        tire = tire[cur]
        #如果已经走到了底部，则添加
        if '#' in tire and tire['#'] ==0:
            res.append(s+cur)
            tire['#'] = 1
        #将当前位置标记为走过
        arrs[i][j] = 'visited'
        #然后四个方向开始遍历
        for dx,dy in [[-1,0],[0,-1],[0,1],[1,0]]:
            ti = dx+i
            tj = dy+j
            if 0<=ti<len(arrs) and 0<=tj<len(arrs[0]) and arrs[ti][tj] != 'visited':
                dfs(ti,tj,tire,s+cur)
            #复位
            arrs[i][j] = cur
        
    
    for i in range(len(arrs)):
        for j in range(len(arrs[0])):
            dfs(i,j,tire,'')
    return res 




board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]

words = ["oath","pea","eat","rain"]
print(findWords(board,words))
