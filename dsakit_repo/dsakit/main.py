"""CLI entrypoint for dsakit demos."""
from linkedlist import SinglyLinkedList
from stack import Stack
from queue import Queue
from tree import BinaryTree, TreeNode
from graph import Graph
from algorithms import bubble_sort, binary_search, linear_search
def demo_linked_list():
    print('LinkedList demo:')
    ll = SinglyLinkedList(); [ll.append(x) for x in [10,20,30]]; print('Init ->', ll)
    ll.reverse(); print('Reversed ->', ll)
def demo_all():
    demo_linked_list()
    print('\nStack/Queue demo:')
    s = Stack(); [s.push(x) for x in [1,2,3]]; print(s); print('pop->', s.pop())
    q = Queue(); [q.enqueue(x) for x in ['a','b']]; print(q); print('deq->', q.dequeue())
    print('\nTree demo:')
    n1 = TreeNode(1); n2 = TreeNode(2); n3 = TreeNode(3); n1.left, n1.right = n2, n3
    bt = BinaryTree(n1); print('Inorder', bt.inorder())
    print('\nGraph demo:')
    g = Graph(); g.add_edge('A','B'); g.add_edge('A','C'); print(g); print('BFS A', g.bfs('A'))
    print('\nAlgorithms demo:'); arr=[5,1,4,2]; print('bubble', bubble_sort(arr)); print('bin idx', binary_search(sorted(arr),4))
if __name__ == '__main__':
    demo_all()
