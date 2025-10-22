import pytest
from main import Solution

@pytest.fixture
def solution():
    """Provides a Solution instance for the tests."""
    return Solution()

def test_empty_list(solution):
    """Tests encoding and decoding an empty list."""
    strs = []
    encoded = solution.encode(strs)
    assert encoded == ""
    decoded = solution.decode(encoded)
    assert decoded == strs

def test_single_string(solution):
    """Tests a list with a single string."""
    strs = ["hello"]
    encoded = solution.encode(strs)
    assert encoded == "5#hello"
    decoded = solution.decode(encoded)
    assert decoded == strs

def test_multiple_strings(solution):
    """Tests a list with multiple simple strings."""
    strs = ["hello", "world"]
    encoded = solution.encode(strs)
    assert encoded == "5#hello5#world"
    decoded = solution.decode(encoded)
    assert decoded == strs

def test_strings_with_delimiter(solution):
    """Tests strings that contain the '#' delimiter."""
    strs = ["neet#code", "is", "awesome#problem"]
    encoded = solution.encode(strs)
    assert encoded == "9#neet#code2#is15#awesome#problem"
    decoded = solution.decode(encoded)
    assert decoded == strs

def test_strings_with_empty_strings(solution):
    """Tests a list containing empty strings."""
    strs = ["", "abc", "", "defg"]
    encoded = solution.encode(strs)
    assert encoded == "0#3#abc0#4#defg"
    decoded = solution.decode(encoded)
    assert decoded == strs
