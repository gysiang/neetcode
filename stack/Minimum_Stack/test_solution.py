import pytest
from main import MinStack

@pytest.fixture
def stack():
    """Provides a fresh MinStack instance for each test."""
    return MinStack()

def test_push_and_top(stack):
    """Tests that push adds an element and top returns it."""
    stack.push(5)
    assert stack.top() == 5
    stack.push(10)
    assert stack.top() == 10

def test_getMin_after_pushes(stack):
    """Tests that getMin returns the correct minimum as elements are pushed."""
    stack.push(-2)
    assert stack.getMin() == -2
    stack.push(0)
    assert stack.getMin() == -2  # Minimum should still be -2
    stack.push(-3)
    assert stack.getMin() == -3  # Minimum should now be -3

def test_pop_updates_top(stack):
    """Tests that pop removes the top element and top is updated."""
    stack.push(1)
    stack.push(2)
    stack.pop()
    assert stack.top() == 1

def test_getMin_after_popping_minimum(stack):
    """Tests that getMin updates correctly after the minimum element is popped."""
    stack.push(10)
    stack.push(5)   # Current min is 5
    stack.push(2)   # Current min is 2
    assert stack.getMin() == 2
    stack.pop()     # Pop 2
    assert stack.getMin() == 5   # New min should be 5
    stack.pop()     # Pop 5
    assert stack.getMin() == 10  # New min should be 10

def test_full_sequence(stack):
    """Tests a sequence of operations as seen in common examples."""
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    assert stack.getMin() == -3   # min is -3
    stack.pop()
    assert stack.top() == 0       # top is 0
    assert stack.getMin() == -2   # min is now -2
