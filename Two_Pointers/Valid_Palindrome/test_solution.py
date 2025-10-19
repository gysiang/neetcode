import pytest
from main import Solution  # Adjust import path as needed
@pytest.fixture
def sol():
    return Solution()

def test_empty_string(sol):
    assert sol.isPalindrome("") is True  # empty string returns False per your code

def test_single_character(sol):
    assert sol.isPalindrome("a") is True

def test_simple_palindrome(sol):
    assert sol.isPalindrome("racecar") is True

def test_mixed_case_palindrome(sol):
    assert sol.isPalindrome("RaceCar") is True

def test_palindrome_with_non_alnum(sol):
    assert sol.isPalindrome("A man, a plan, a canal: Panama") is True

def test_non_palindrome(sol):
    assert sol.isPalindrome("hello") is False

def test_only_non_alphanumeric(sol):
    assert sol.isPalindrome("!!!") is True  # no alnums means left >= right quickly, returns True

def test_spaces_and_punctuation(sol):
    assert sol.isPalindrome("No lemon, no melon") is True

def test_numeric_palindrome(sol):
    assert sol.isPalindrome("12321") is True

def test_numeric_non_palindrome(sol):
    assert sol.isPalindrome("12345") is False
