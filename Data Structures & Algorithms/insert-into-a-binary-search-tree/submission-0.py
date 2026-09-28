# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        val_node = TreeNode(val)
        if not root:
            return val_node

        curr = root

        while True:
            if val > curr.val:
                if curr.right is None:
                    curr.right = val_node
                    break
                curr = curr.right
            else:
                if curr.left is None:
                    curr.left = val_node
                    break
                curr = curr.left

        return root