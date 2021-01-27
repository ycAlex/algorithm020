#LRU借助双向链表+字典来实现
#字典：快速定位是否存在-同时需要思考字典的key,value分别是什么
#双向链表：可以快速的定位到头部和尾部

#定义双向链表
class ListNode:
	def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
    

class LRU:
    #初始化双向链表和一个字典
    def __init__(self, capacity:int):
        self.cap = capacity
        self.dic = {}
        self.head = ListNode(None,None)
        self.tail = ListNode(None,None)
        self.head.next = self.tail
        self.tail.prev = self.head 
    #双向链表的插入-头插
    def insert(self,newNode):
        #先获取头部后面的
        tmp = self.head.next
        #将新节点放入头部后
        self.head.next = newNode
        #新节点的后面就是tmp
        newNode.next = tmp
        #新节点的前面是头部
        newNode.prev = head
        #tmp的前面从头部变为新节点
        tmp.prev = newNode 
        
    #删除双向链表里面的节点
    def delete(self,node):
        #删除节点的前一个的下一个为删除节点的下一个
        node.prev.next = node.next 
        #删除节点的下一个的前一个为删除节点的前一个
        node.next.prev = node.prev 
    #实现LRU的get
    def get(self,key):
        #如果不在字典里面，直接返回-1，不用遍历双向链表了
        if key not in dic:
            return -1
        #如果有，通过进来的key获取到node
        node = self.dic[key]
        #先删除，再插入头部，更新此节点的位置
        self.delete(node)
        self.insert(node)
        return node.val
    #LRU的put
    def put(self,key,val):
        #如果已经有了
        if key in dic:
            #得到此节点
            node = dic[key]
            #然后更新节点的value
            node.val = val
            #删除先，再插回头部
            self.delete(node)
            self.insert(node)
            return 
        #如果没有的情况，看是否满了
        if len(self.dic)==self.cap:
            #如果满了，先把最后一个删掉
            tmp = self.tail.prev
            self.delete(tmp)
            del self.dic[tmp.key]
        #然后建立新节点
        node = ListNode(key,val)
        #更新字典，更新链表
        self.dic[key] = node
        self.insert(node)

