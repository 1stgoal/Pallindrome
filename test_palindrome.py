"""
Tests the palindrome module
"""

import pytest
from palindrome import is_palindrome


# is_palindrome raises a ValueError when not str.
def test_not_string():
    with pytest.raises(ValueError):
        is_palindrome(7172)




