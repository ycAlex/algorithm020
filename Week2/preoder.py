#我觉得前序遍历代码是次要的，关键是得明白遍历顺序
#递归就不说了，迭代的关键是如何对栈的运用，因为是根左右的顺序，要保证每次往下走，左边要先出栈，所有每次左子树要后入栈
#https://leetcode-cn.com/problems/binary-tree-preorder-traversal/solution/144-er-cha-shu-de-qian-xu-bian-li-di-gui-die-dai-3/

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        st  = [root]
        res = []
        while(st):
            cur = st.pop()
            res.append(cur.val)
            if cur.right:
                st.append(cur.right)
            if cur.left:
                st.append(cur.left)
        return res
        
        '''
        res = []
        if root:
            res+= [root.val]
            res+= self.preorderTraversal(root.left)
            res+= self.preorderTraversal(root.right)
        return res
        '''


        '''
        res = []
        def helper(root):
            if not root:
                return 
            res.append(root.val)
            helper(root.left)
            helper(root.right)
        helper(root)
        return res
        '''