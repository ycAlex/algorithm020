#中序遍历其实和前序一样，关键是如何保障出栈顺序
#其实思路比前序多绕了一个弯，因为中序是左根右，所以为了保证是左子树先入res，但是要想法记录下来根以便能回溯
#https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/94-er-cha-shu-de-zhong-xu-bian-li-die-dai-di-gui-b/

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        st = []
        res = []
        while st or root:
            if root:
                st.append(root)
                root = root.left
            else:
                tmp = st.pop()
                res.append(tmp.val)
                root = tmp.right
        return res

        '''
        res = []
        def helper(root):
            if not root:
                return 
            helper(root.left)
            res.append(root.val)
            helper(root.right)
        helper(root)
        return res
        '''
        '''
        res = []
        if root:
            res+=self.inorderTraversal(root.left)
            res+=[root.val]
            res+=self.inorderTraversal(root.right)
        return res
        '''