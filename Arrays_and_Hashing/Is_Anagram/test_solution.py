import pytest
from main import Solution

@pytest.fixture
def sol():
    """Provides a Solution instance for the tests."""
    return Solution()

def test_valid_anagram(sol):
    """Test a simple valid anagram."""
    assert sol.isAnagram("anagram", "nagaram") is True

def test_invalid_anagram(sol):
    """Test a simple invalid anagram."""
    assert sol.isAnagram("rat", "car") is False

def test_different_lengths(sol):
    """Test strings of different lengths, which cannot be anagrams."""
    assert sol.isAnagram("a", "ab") is False
    assert sol.isAnagram("hello", "hell") is False

def test_repeated_characters(sol):
    """Test anagrams with repeated characters."""
    assert sol.isAnagram("aacc", "ccaa") is True

def test_empty_strings(sol):
    """Test two empty strings, which are considered anagrams."""
    assert sol.isAnagram("", "") is True

def test_unicode_characters(sol):
    """Test with unicode characters."""
    assert sol.isAnagram("你好", "好你") is True

def test_same_characters_different_counts(sol):
    """Test strings with same characters but different frequencies."""
    assert sol.isAnagram("aab", "abb") is False
