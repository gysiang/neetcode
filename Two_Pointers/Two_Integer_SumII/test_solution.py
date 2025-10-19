import pytest
from main import Solution  # Import your Solution class

@pytest.fixture
def sol():
    return Solution()

def test_empty_input(sol):
    assert sol.twoSum([], 5) == []

def test_no_solution(sol):
    assert sol.twoSum([1, 2, 3], 10) == []

def test_single_pair(sol):
    assert sol.twoSum([1, 2, 3, 4, 6], 10) == [[3, 4]]

def test_multiple_pairs(sol):
    assert sol.twoSum([1, 2, 3, 4, 5, 6], 7) == [[0, 5], [1, 4], [2, 3]]

def test_duplicates(sol):
    assert sol.twoSum([2, 2, 2, 2], 4) == [[0, 3], [1, 2]]

def test_negative_numbers(sol):
    assert sol.twoSum([-3, -1, 0, 1, 3], 0) == [[0, 4], [1, 3]]

def test_all_zeroes(sol):
    assert sol.twoSum([0, 0, 0, 0], 0) == [[0, 3], [1, 2]]
