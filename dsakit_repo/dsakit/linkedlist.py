from typing import Any, Optional, List
class LLNode:
    def __init__(self, val: Any):
        self.val = val
        self.next: Optional['LLNode'] = None
    def __repr__(self):
        return str(self.val)
class SinglyLinkedList:
    def __init__(self):
        self.head: Optional[LLNode] = None
    def append(self, val: Any) -> None:
        node = LLNode(val)
        if not self.head:
            self.head = node; return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node
    def prepend(self, val: Any) -> None:
        node = LLNode(val); node.next = self.head; self.head = node
    def find(self, val: Any) -> Optional[LLNode]:
        cur = self.head
        while cur:
            if cur.val == val: return cur
            cur = cur.next
        return None
    def delete(self, val: Any) -> bool:
        prev, cur = None, self.head
        while cur:
            if cur.val == val:
                if prev: prev.next = cur.next
                else: self.head = cur.next
                return True
            prev, cur = cur, cur.next
        return False
    def reverse(self) -> None:
        prev, cur = None, self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev
    def to_list(self) -> List[Any]:
        out = []; cur = self.head
        while cur: out.append(cur.val); cur = cur.next
        return out
    def __repr__(self):
        return '->'.join(map(str, self.to_list())) or 'EmptyList'
