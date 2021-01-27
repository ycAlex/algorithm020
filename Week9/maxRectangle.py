##计算矩形面积这里和柱状图的最大面积一样，通过栈来得到长度

#这里借鉴柱状图最大面积的计算方法，通过栈
def calcArea(heights):
    heights = [0]+heights+[0]
    #保存前面走过的下标，通过下标计算length
    st = []
    res = 0
    #遍历高度
    for i in range(len(heights)):
        #如果前面的大于当前的，则可能构成矩形面积更大，因为高更大了
        while st and heights[st[-1]]>heights[i]:
            #拿出高的位置
            sth = st.pop(-1)
            #比较面积，看是上一个最大的大，还是新的面积大
            res = max(res, heights[sth] * (i - st[-1] - 1))
        st.append(i)
    return res 

def maxRectangle(arrs):
    if not arrs:return 0
    
    ans = 0
    heights = [0]*len(arrs[0])
    #记录下行对应的高度
    for i in range(len(arrs)):
        for j in range(len(arrs[0])):
            if arrs[i][j] =='1':
                heights[j]+=1
            else:
                heights[j] = 0
        #走完一行开始计算是否有最大面积
        ans = max(ans,calcArea(heights))
    return ans 

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

print(maxRectangle(matrix))
    
	