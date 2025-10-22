import pytest
from main import Solution

def sort_grouped_anagrams(groups: list[list[str]]) -> list[list[str]]:
    """
    Sorts the inner lists and the outer list for deterministic comparison.
    The order of the groups and the strings within them is not guaranteed by the function.
    """
    for group in groups:
        group.sort()
    groups.sort(key=lambda x: x[0] if x else "")
    return groups

@pytest.fixture
def sol():
    """Provides a Solution instance for the tests."""
    return Solution()

def test_example_case(sol):
    """Test the primary example from the problem description."""
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    result = sol.groupAnagrams(strs)
    assert sort_grouped_anagrams(result) == sort_grouped_anagrams(expected)

def test_empty_list(sol):
    """Test with an empty input list."""
    strs = []
    expected = []
    assert sol.groupAnagrams(strs) == expected

def test_single_string(sol):
    """Test with a list containing a single string."""
    strs = ["a"]
    expected = [["a"]]
    assert sol.groupAnagrams(strs) == expected

def test_no_anagrams(sol):
    """Test with a list where no strings are anagrams of each other."""
    strs = ["abc", "def", "ghi"]
    expected = [["abc"], ["def"], ["ghi"]]
    result = sol.groupAnagrams(strs)
    assert sort_grouped_anagrams(result) == sort_grouped_anagrams(expected)

def test_empty_strings(sol):
    """Test with empty strings in the list."""
    strs = ["", "b", ""]
    expected = [["", ""], ["b"]]
    result = sol.groupAnagrams(strs)
    assert sort_grouped_anagrams(result) == sort_grouped_anagrams(expected)
