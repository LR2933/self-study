"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = [root]
        ret = []
        while stack != []:
            node = stack.pop()
            ret.append(node.val)
            if node.children != []:
                stack.extend(node.children)
        return reversed(ret)

