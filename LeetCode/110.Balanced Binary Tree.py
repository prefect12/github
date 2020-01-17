'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.


'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.aux_ba(root)[1]

    def aux_ba(self, current):
        if not current:
            return [0, True]
        else:
            [level1, statu1] = self.aux_ba(current.left)
            [level2, statu2] = self.aux_ba(current.right)
            return [max(level1, level2) + 1, abs(level1 - level2) - 1 <= 0 and (statu1 and statu2)]
