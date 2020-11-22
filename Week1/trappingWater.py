#借用栈，就是找V-其实也是找w，个人理解就是W可以是N个V叠加，下面是我的详细题解，不知道理解的对否
#https://leetcode-cn.com/problems/trapping-rain-water/solution/jie-yong-zhan-lai-ji-lu-yi-ge-di-jian-de-shu-zu-by/
def trap(self, height: List[int]) -> int:
        if len(height)<3:
            return 0

        res,inx = 0,0
        st = []
        while(inx<len(height)):
            while st and height[st[-1]]<height[inx]:
                bottom = st.pop(-1)
                if len(st)==0:
                    break
                newHeight = min(height[st[-1]],height[inx]) - height[bottom]
                area = newHeight*(inx-st[-1]-1)
                res+=area
            st.append(inx)
            inx+=1
        
        return res

