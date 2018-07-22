"""
描述
设计一个算法，并编写代码来序列化和反序列化二叉树。将树写入一个文件被称为“序列化”，读取文件后重建同样的二叉树被称为“反序列化”。

如何反序列化或序列化二叉树是没有限制的，你只需要确保可以将二叉树序列化为一个字符串，并且可以将字符串反序列化为原来的树结构。

There is no limit of how you deserialize or serialize a binary tree, LintCode will take your output of serialize as the input of deserialize, it won't check the result of serialize.

样例
给出一个测试数据样例， 二叉树{3,9,20,#,#,15,7}，表示如下的树结构：

  3
 / \
9  20
  /  \
 15   7
我们的数据是进行BFS遍历得到的。当你测试结果wrong answer时，你可以作为输入调试你的代码。

你可以采用其他的方法进行序列化和反序列化。
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        # write your code here
        data = []
        data += root.val
        if root.left is not None:
            # data += root.left.val
            data += self.serialize(root.left))
        else:
            data += ['#']
        if root.right is not None:
            # data += root.right.val
            data += self.serialize(root.right))
        else:
            data += ['#']
        return data

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """
    def deserialize(self, data):
        # write your code here
        root = TreeNode()
        if len(data) == 1:
            root.val = data[0]
        elif len(data) == 2:
            root.val = data[0]
            root.left = TreeNode(data[1])
        elif len(data) == 3:
            root.val = data[0]
            if data[1] != '#':
                root.left = TreeNode(data[1])
            root.left = TreeNode(data[2])
        else:
            val, left, right, *new_data = data
            root.val = val
            if left != '#':
                root.left = TreeNode(left)
            if right != '#':
                root.left = TreeNode(data[2])
           
        return root 
