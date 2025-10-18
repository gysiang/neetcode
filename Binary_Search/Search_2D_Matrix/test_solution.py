from main import Solution

def test_search_matrix_found():
    s = Solution()
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    assert s.searchMatrix(matrix, 3) is True

def test_search_matrix_empty():
    s = Solution()
    matrix = []
    assert s.searchMatrix(matrix, 1) is False

def test_search_matrix_single_row():
    s = Solution()
    matrix = [[1, 2, 3, 4, 5]]
    assert s.searchMatrix(matrix, 4) is True
    assert s.searchMatrix(matrix, 6) is False

def test_search_matrix_single_column():
    s = Solution()
    matrix = [[1], [3], [5]]
    assert s.searchMatrix(matrix, 3) is True
    assert s.searchMatrix(matrix, 2) is False
