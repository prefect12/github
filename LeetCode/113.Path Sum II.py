'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]


'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.alist = []
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.aux_path(root,[],sum)
        return self.alist
    def aux_path(self,cur_node,current,add):
        if not cur_node:
                return
        if not cur_node.left and not cur_node.right:
            if sum(current) + cur_node.val == add:
                current.append(cur_node.val)
                self.alist.append(current[:])
            return
        current.append(cur_node.val)
        self.aux_path(cur_node.left,current[:],add)
        self.aux_path(cur_node.right,current[:],add)
        return