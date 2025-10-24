import pytest
from main import Solution

@pytest.fixture
def solution():
    """Provides a Solution instance for the tests."""
    return Solution()

def test_general_case(solution):
    """Tests a standard list of positive integers."""
    nums = [1, 2, 3, 4]
    expected = [24, 12, 8, 6]
    assert solution.productExceptSelf(nums) == expected

def test_with_zero(solution):
    """Tests a list containing one zero."""
    nums = [1, 2, 0, 4]
    expected = [0, 0, 8, 0]
    assert solution.productExceptSelf(nums) == expected

def test_with_multiple_zeros(solution):
    """Tests a list containing more than one zero."""
    nums = [1, 0, 3, 0]
    expected = [0, 0, 0, 0]
    assert solution.productExceptSelf(nums) == expected

def test_with_negative_numbers(solution):
    """Tests a list containing negative numbers."""
    nums = [-1, 1, 2, -3, 3]
    expected = [-18, 18, 9, -6, 6]
    assert solution.productExceptSelf(nums) == expected

def test_two_elements(solution):
    """Tests the edge case of a two-element list."""
    nums = [5, 10]
    expected = [10, 5]
    assert solution.productExceptSelf(nums) == expected

def test_all_same_elements(solution):
    """Tests a list where all elements are the same."""
    nums = [5, 5, 5, 5]
    expected = [125, 125, 125, 125]
    assert solution.productExceptSelf(nums) == expected
