import pytest
from main import Solution

@pytest.fixture
def sol():
    """Provides a Solution instance for the tests."""
    return Solution()

def test_simple_operations(sol):
    """Tests basic arithmetic operations."""
    assert sol.evalRPN(["2", "1", "+"]) == 3
    assert sol.evalRPN(["4", "2", "-"]) == 2
    assert sol.evalRPN(["3", "5", "*"]) == 15
    assert sol.evalRPN(["10", "5", "/"]) == 2

def test_longer_expression(sol):
    """Tests a longer, more complex expression."""
    tokens = ["4", "13", "5", "/", "+"]
    # Calculation: 4 + (13 / 5) -> 4 + 2 = 6
    assert sol.evalRPN(tokens) == 6

def test_expression_with_negative_numbers(sol):
    """Tests an expression involving negative numbers."""
    tokens = ["10", "-5", "+"]
    assert sol.evalRPN(tokens) == 5

def test_division_truncation(sol):
    """Tests that division truncates towards zero."""
    # 6 / -132 -> -0.045... -> 0
    assert sol.evalRPN(["6", "-132", "/"]) == 0
    # 13 / 5 -> 2.6 -> 2
    assert sol.evalRPN(["13", "5", "/"]) == 2
    # -13 / 5 -> -2.6 -> -2
    assert sol.evalRPN(["-13", "5", "/"]) == -2

def test_complex_leet_code_example(sol):
    """Tests a complex example from the problem description."""
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    # A bit-by-bit evaluation leads to 22
    assert sol.evalRPN(tokens) == 22
