# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution2:
    def isSameTree(self, p, q) -> bool:
        return self.aux_isSameTree(p, q)

    def aux_isSameTree(self, left, right):
        if left == right == None:
            return True
        elif (left == None and right != None) or (right == None and left != None):
            return False
        elif (left.left == left.right == right.left == right.right == None) and (left.val == right.val):
            return True

        if left.val == right.val:
            return self.aux_isSameTree(left.left, right.left) and self.aux_isSameTree(left.right, right.right)
        return False


# ===============================
class Solution:

    def aux_isSameTree(self, p, q):

        if p is None and q is None:
            return True
        elif (p is None and q is not None) or (p is not None and q is None):
            return False
        if p.val == q.val:
            return self.aux_isSameTree(p.left, q.left) and self.aux_isSameTree(p.right, q.right)
        return False

    def isSameTree(self, p, q):

        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.aux_isSameTree(p, q)

