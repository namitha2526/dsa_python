from typing import Any, Optional, List
from collections import deque
class TreeNode:
    def __init__(self, val: Any):
        self.val = val; self.left: Optional['TreeNode'] = None; self.right: Optional['TreeNode'] = None
    def __repr__(self): return str(self.val)
class BinaryTree:
    def __init__(self, root: Optional[TreeNode] = None):
        self.root = root
    def inorder(self) -> List[Any]:
        out = []
        def _in(n):
            if not n: return
            _in(n.left); out.append(n.val); _in(n.right)
        _in(self.root); return out
    def preorder(self) -> List[Any]:
        out = []
        def _pre(n):
            if not n: return
            out.append(n.val); _pre(n.left); _pre(n.right)
        _pre(self.root); return out
    def postorder(self) -> List[Any]:
        out = []
        def _post(n):
            if not n: return
            _post(n.left); _post(n.right); out.append(n.val)
        _post(self.root); return out
    def level_order(self) -> List[List[Any]]:
        if not self.root: return []
        q = deque([self.root]); levels = []
        while q:
            sz = len(q); level = []
            for _ in range(sz):
                node = q.popleft(); level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            levels.append(level)
        return levels
