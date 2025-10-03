from dsakit.linkedlist import SinglyLinkedList
def test_linkedlist_append_reverse():
    ll = SinglyLinkedList()
    for i in range(4): ll.append(i)
    assert ll.to_list() == [0,1,2,3]
    ll.reverse()
    assert ll.to_list() == [3,2,1,0]
