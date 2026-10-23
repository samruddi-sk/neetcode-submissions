class Codec:

    def serialize(self, root):
        result = []

        def preorder(node):
            if not node:
                result.append("null")
                return

            result.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ",".join(result)

    def deserialize(self, data):
        values = iter(data.split(","))

        def build():
            val = next(values)

            if val == "null":
                return None

            node = TreeNode(int(val))
            node.left = build()
            node.right = build()

            return node

        return build()