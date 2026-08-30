# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_valid(self, node, min_val, max_val):
        if node is None :
            return True
        if node.val <= min_val or node.val >= max_val: 
            return False
        left_isValid=self.is_valid(node.left,min_val,node.val)
        right_isValid=self.is_valid(node.right,node.val,max_val)
        return left_isValid and right_isValid
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.is_valid(root, float('-inf'), float('inf'))
    
            


        