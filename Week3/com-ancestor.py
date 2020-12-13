#其实这道题就是我在README里面所说的，回溯并一定是要通过删除，这里通过返回节点来实现回溯！
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or p==root or q ==root:
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if not root.left and not root.right:
            return 
        if not left:
            return right
        if not right:
            return left
        return root #if left and right

