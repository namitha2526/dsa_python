import pytest
from dsakit.stack import Stack
def test_stack_push_pop():
    s = Stack(); s.push(1); s.push(2)
    assert len(s) == 2
    assert s.pop() == 2
    assert s.pop() == 1
    with pytest.raises(IndexError):
        s.pop()
