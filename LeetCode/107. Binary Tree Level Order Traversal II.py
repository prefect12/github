'''

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
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
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.aux_leve(root,0)
        self.alist.reverse()
        return self.alist
    def aux_leve(self,current,level):
        if not current:
            return 0
        else:
            if len(self.alist) <= level:
                self.alist.append([])
            self.alist[level].append(current.val)
            self.aux_leve(current.left,level+1)
            self.aux_leve(current.right,level+1)