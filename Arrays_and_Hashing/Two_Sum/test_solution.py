import pytest
from main import Solution

@pytest.fixture
def sol():
    """Provides a Solution instance for the tests."""
    return Solution()

def test_basic_positive_numbers(sol):
    """Test with basic positive numbers."""
    nums = [2, 7, 11, 15]
    target = 9
    assert sorted(sol.twoSum(nums, target)) == sorted([0, 1])

def test_different_order(sol):
    """Test with numbers in a different order."""
    nums = [15, 7, 2, 11]
    target = 9
    assert sorted(sol.twoSum(nums, target)) == sorted([1, 2]) # 7 at index 1, 2 at index 2

def test_negative_numbers(sol):
    """Test with negative numbers."""
    nums = [-1, -2, -3, -4, -5]
    target = -8
    assert sorted(sol.twoSum(nums, target)) == sorted([2, 4]) # -3 at index 2, -5 at index 4

def test_mixed_numbers(sol):
    """Test with mixed positive and negative numbers."""
    nums = [-3, 4, 3, 90]
    target = 0
    assert sorted(sol.twoSum(nums, target)) == sorted([0, 2]) # -3 at index 0, 3 at index 2

def test_duplicate_numbers(sol):
    """Test with duplicate numbers in the input array."""
    nums = [3, 3]
    target = 6
    assert sorted(sol.twoSum(nums, target)) == sorted([0, 1])
