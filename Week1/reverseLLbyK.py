#不确定我这的写会不会太啰嗦了，面试中这样写不知道行不行？
#https://leetcode-cn.com/problems/reverse-nodes-in-k-group/solution/ji-yu-fan-zhuan-lian-biao-zhe-ying-gai-shi-zui-jia/

def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        #初始化一个list，然后指向head
        res = ListNode(0)
        res.next = head
        #一个当前结果的指针，开始指向了res，也就是head之前-上面提到的tmp指针里面的第一个
        cur = res

        #开始遍历head
        while(head):
            #moves指针-是记录我们每次走k次之前的位置，tmp指针里面的第二个
            moves = head
            #看还能否走K个
            count = 0
            while(count<k and head):
                head = head.next
                count+=1
            #如果不能走k个，则直接返回
            if count!=k:
                return res.next
            
            #反转K个
            tmpList = None  
            while(moves!=head):
                tmp = moves.next
                moves.next = tmpList
                tmpList =moves
                moves= tmp
            
            #将反转之后的K个拼接到res上面
            cur.next = tmpList
            
            #移动到拼接之后的res的尾部
            while(cur.next):
                cur= cur.next

            #将反转的K个之后的部分再拼接回去
            cur.next = head
            #print(cur)
        #返回结果
        return res.next
