#==========================================================================================
# https://neetcode.io/problems/invert-a-binary-tree?list=neetcode150
#
# Solve this problem by recognizing we can use recursion to traverse the tree. As we make \
# each traversal we can swap the left and right for the node we are currently on and then \
# vist the left and right of each node we just swapped and do the same, base case is that \
# the node doesn't exist and at that point we go back up our stack and return the root \
# node which the solution for our problem here.
#
#==========================================================================================


from typing import Optional

class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invert_binary_tree(self, node: TreeNode) -> Optional[TreeNode]:
        if not node:
            return
        elif node:
            temp = node.left
            node.left = node.right
            node.right = temp
            self.invert_binary_tree(node.left)
            self.invert_binary_tree(node.right)

        return node




right_right = TreeNode(8)

left_left = TreeNode(6)
left_right = TreeNode(5)

right = TreeNode(4, None, right_right)
left = TreeNode(3, left_left, left_right)

root = TreeNode(2, left, right)

test = Solution()

print(root.left, root.right)

print(test.invert_binary_tree(root))

print(root.left, root.right)