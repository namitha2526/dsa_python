from typing import Any, List
class Stack:
    def __init__(self):
        self._data: List[Any] = []
    def push(self, v: Any) -> None: 
        self._data.append(v)
    def pop(self) -> Any:
        if not self._data:
            raise IndexError('pop from empty stack')
        return self._data.pop()
    def peek(self):
        return self._data[-1] if self._data else None
    def is_empty(self) -> bool:
        return not self._data
    def __len__(self):
        return len(self._data)
    def __repr__(self):
        return f"Stack(top->bottom): {list(reversed(self._data))}"
