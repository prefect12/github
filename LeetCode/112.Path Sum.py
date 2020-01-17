'''

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1


'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        return self.aux_has(root, 0, sum)

    def aux_has(self, cur_node, current, sum):
        if not cur_node:
            return False
        m = cur_node.val + current
        if not cur_node.left and not cur_node.right:
            if m == sum:
                return True
            if m != sum:
                return False
        return self.aux_has(cur_node.left, m, sum) or self.aux_has(cur_node.right, m, sum)
