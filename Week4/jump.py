#这道题因为说了必能到达终点，所以求最小的时候，必然是跳最大的
#个人感觉可以这样理解-每次跳会覆盖1-N个，然后把下面的1-N个看成一组再找里面最大的作为新的起点
#重复上述步骤，直到走到尾部

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        res = 0 
        inx = 0
        maxsteps = 0
        #最远步骤到达了最后一个就停
        #确定终止条件
        while(maxsteps<len(nums)-1):
            #保存下来每次跳跃能达到的后面的几个的值
            #也就是思路里面所说的新的一组
            tmp = []
            #如果是在此次跳跃所能到达的范围，则找出来那个最大的
            #关键是这里-要知道什么条件下我们可以移动下标，只有被覆盖到的才可以开始移动
            while(inx<=maxsteps):
                tmp.append(inx+nums[inx])
                inx+=1
            maxsteps = max(tmp)
            res+=1
        return res 

#https://leetcode-cn.com/problems/jump-game-ii/solution/45-tiao-yue-you-xi-ii-tan-xin-by-alex11-lqyo/
