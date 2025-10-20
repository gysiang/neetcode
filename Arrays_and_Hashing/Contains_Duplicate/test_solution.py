import pytest
from main import Solution

@pytest.fixture
def sol():
    """Provides a Solution instance for the tests."""
    return Solution()

def test_no_duplicates(sol):
    """Test a list with all unique elements."""
    assert sol.hasDuplicate([1, 2, 3, 4, 5]) is False

def test_with_duplicates(sol):
    """Test a list with a simple duplicate."""
    assert sol.hasDuplicate([1, 2, 3, 1]) is True

def test_empty_list(sol):
    """Test an empty list, which has no duplicates."""
    assert sol.hasDuplicate([]) is False

def test_single_element_list(sol):
    """Test a list with one element."""
    assert sol.hasDuplicate([10]) is False

def test_all_elements_are_duplicates(sol):
    """Test a list where all elements are the same."""
    assert sol.hasDuplicate([5, 5, 5, 5]) is True

def test_duplicates_at_beginning(sol):
    """Test a list with duplicates at the start."""
    assert sol.hasDuplicate([2, 2, 3, 4]) is True

def test_with_negative_numbers(sol):
    """Test a list containing negative numbers and duplicates."""
    assert sol.hasDuplicate([-1, 0, 5, -1]) is True
