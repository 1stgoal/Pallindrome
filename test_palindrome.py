"""
Tests the palindrome module
"""

import pytest
from palindrome import is_palindrome


# is_palindrome raises a ValueError when not str.
def test_not_string():
    with pytest.raises(ValueError):
        is_palindrome(7172)


# is_palindrome returns False when called with an empty string.

def test_empty_string():
    assert not is_palindrome("")


# is_palindrome returns True if called with "a".
def test_string_a():
    assert is_palindrome("a")


# is_palindrome returns True if called with "a".
def test_string_a():
    assert is_palindrome("a")


# is_palindrome returns True if called with "bb"
def test_string_bb():
    assert is_palindrome("bb")
