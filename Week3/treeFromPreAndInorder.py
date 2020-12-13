#其实这道题就需要明白两点：1.如果通过前序和中序拿到每一次的根。
#2，知道使用递归，根据1中拿到新的根来分生产新的子树

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        inx = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:inx+1],inorder[:inx])
        root.right = self.buildTree(preorder[inx+1:],inorder[inx+1:])
        return root