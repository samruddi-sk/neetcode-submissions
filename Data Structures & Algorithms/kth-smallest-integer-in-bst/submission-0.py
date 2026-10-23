class Solution:
    def kthSmallest(self, root, k):
        nums = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)

        inorder(root)
        return nums[k - 1]