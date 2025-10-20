import pytest
from main import Solution

@pytest.fixture
def sol():
    """Provides a Solution instance for the tests."""
    return Solution()

# --- Valid Cases ---

def test_empty_string(sol):
    """Test an empty string, which should be valid."""
    assert sol.isValid("") is True

def test_simple_valid_pairs(sol):
    """Test simple, non-nested valid pairs."""
    assert sol.isValid("()") is True
    assert sol.isValid("[]") is True
    assert sol.isValid("{}") is True

def test_multiple_valid_pairs(sol):
    """Test a sequence of valid pairs."""
    assert sol.isValid("()[]{}") is True

def test_nested_valid_pairs(sol):
    """Test nested valid pairs."""
    assert sol.isValid("{[]}") is True
    assert sol.isValid("([{}])") is True

def test_complex_valid_string(sol):
    """Test a more complex but valid string."""
    assert sol.isValid("({[]})") is True

# --- Invalid Cases ---

def test_mismatched_closing_bracket(sol):
    """Test cases where closing brackets do not match the opening ones."""
    assert sol.isValid("(]") is False
    assert sol.isValid("([)]") is False

def test_unclosed_opening_bracket(sol):
    """Test cases with unclosed opening brackets."""
    assert sol.isValid("(") is False
    assert sol.isValid("[{") is False
    assert sol.isValid("(()") is False

def test_closing_bracket_first(sol):
    """Test cases where a closing bracket appears before any opening bracket."""
    assert sol.isValid(")") is False
    assert sol.isValid("())") is False
    assert sol.isValid("}}") is False
