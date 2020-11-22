#就是寻找V，这里也可能是W-可以理解为N个V叠加
#https://leetcode-cn.com/problems/trapping-rain-water/solution/jie-yong-zhan-lai-ji-lu-yi-ge-di-jian-de-shu-zu-by/
def trap(self, height: List[int]) -> int:
        if len(height)<3:
            return 0
        #初始化结果，和一个记录当前的位置的指针
        res,inx = 0,0
        #一个栈来保存V的左侧部分
        st = []
        while(inx<len(height)):
            #如果有可能的左侧部分，则看下一个进来的左侧部分的延续还是右侧部分（再次思考V)
            while st and height[st[-1]]<height[inx]:
                bottom = st.pop(-1)
                if len(st)==0:
                    break
                #如果能形成一个小V，计算这个小V的面积
                newHeight = min(height[st[-1]],height[inx]) - height[bottom]
                area = newHeight*(inx-st[-1]-1)
                res+=area
            st.append(inx)
            inx+=1
        
        return res 

