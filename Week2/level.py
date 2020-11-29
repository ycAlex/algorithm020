#层数遍历-我个人觉得必须是BFS，因为dfs要做回溯其实消耗会比bfs大，所以这道题没练dfs，感觉面试不会傻到要问dfs吧。。。。
#n叉树比二叉树唯一的不同就是如何拿到子节点。
#https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/solution/589ncha-shu-de-qian-xu-bian-li-die-dai-di-gui-by-a/

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if not root:
            return res
        st= [root]
        while (st):
            st2 = []
            r2 = []
            while(st):
                tmp = st.pop(0)
                r2.append(tmp.val)
                for each in tmp.children:
                    st2.append(each)
            res.append(r2)
            st = st2
            #st = st2[::-1]
        
        return res