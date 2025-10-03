from collections import deque
from typing import Any
class Queue:
    def __init__(self):
        self._q = deque()
    def enqueue(self, v: Any) -> None:
        self._q.append(v)
    def dequeue(self) -> Any:
        if not self._q:
            raise IndexError('dequeue from empty queue')
        return self._q.popleft()
    def peek(self):
        return self._q[0] if self._q else None
    def is_empty(self) -> bool:
        return not self._q
    def __len__(self):
        return len(self._q)
    def __repr__(self):
        return f"Queue(front->back): {list(self._q)}"
