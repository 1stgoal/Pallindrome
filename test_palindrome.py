"""
Tests the palindrome module
"""

import pytest
from palindrome import is_palindrome


# test_not_string raises a ValueError when not str.
def test_not_string():
    with pytest.raises(ValueError):
        is_palindrome(7172)
