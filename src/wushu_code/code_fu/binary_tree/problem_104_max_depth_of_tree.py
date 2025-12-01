# Example 
# Big idea - Uses recursion to get the depth of each child 
# Base Condition - A leaf returns depth of 0, but current node returns 1 

#maxDepth(3) = max(9,20) + 1 = 2 + 1 aka current node + 2 deep = 3 
#maxDepth(9) = max(0,0) + 1 = 1
#maxDepth(20) = max(15,7) + 1 = 2 
#maxDepth(15) = max(0,0) + 1 = 1
#maxDepth(7) = max(0,0) + 1 = 1


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Problem104: 
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        if root is None: 
            return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        depth = max(left_depth, right_depth) + 1 #given current node 
        return depth
  


def main():
    
    b = Problem104()
    #root = [3,9,20,null,null,15,7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    max_depth = b.maxDepth(root) 
    
    print(f"The max depth is {max_depth}")

if __name__ == "__main__": main()