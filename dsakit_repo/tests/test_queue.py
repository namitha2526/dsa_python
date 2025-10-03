import pytest
from dsakit.queue import Queue
def test_queue_basic():
    q = Queue(); q.enqueue('x'); q.enqueue('y')
    assert q.dequeue() == 'x'
    assert q.dequeue() == 'y'
    import pytest as _pytest
    with _pytest.raises(IndexError):
        q.dequeue()
