class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def maxDepth(node):
            nonlocal diameter

            if not node:
                return 0

            left = maxDepth(node.left)
            right = maxDepth(node.right)

            diameter = max(diameter, left + right)

            return 1 + max(left, right)

        maxDepth(root)
        return diameter