from dsakit.algorithms import bubble_sort, binary_search, linear_search
def test_sort_search():
    arr = [3,1,2]
    assert bubble_sort(arr) == [1,2,3]
    assert binary_search([1,2,3], 2) == 1
    assert linear_search([9,8,7], 8) == 1
