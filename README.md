# dsakit — compact DSA toolkit (Python)

Single-package demo implementing core data structures and algorithms:
- Stack, Queue, Singly Linked List, Binary Tree, Graph
- Utility algorithms: BFS, DFS, sorting/search examples
- Simple CLI entrypoint and pytest unit tests

## How to run
- Python 3.8+ recommended
- Run demos: `python -m dsakit.main`
- Run tests: `pytest -q`

## Structure
- dsakit/        (package)
  - stack.py, queue.py, linkedlist.py, tree.py, graph.py, algorithms.py, main.py, __init__.py
- tests/         (pytest tests)
- .github/workflows/ci.yml  (GitHub Actions)
