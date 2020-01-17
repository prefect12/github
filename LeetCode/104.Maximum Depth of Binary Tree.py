'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.aux_Depth(root, 0)

    def aux_maxDepth2(self, node):
        if not node:
            return 0

        if node.left == None and node.right == None:
            return 1

        else:
            return 1 + max(self.aux_maxDepth(node.left), self.aux_maxDepth(node.right))

    def aux_Depth(self, current, n):
        if not current:
            return n
        return max(self.aux_Depth(current.left, n + 1), self.aux_Depth(current.right, n + 1))