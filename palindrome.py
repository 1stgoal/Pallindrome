# is_palindrome raise ValueError if not str or returns False when empty str or accepts str.
def is_palindrome(value: str) -> bool:
    if not isinstance(value, str):
        raise ValueError
    elif not value:
        return False
    elif isinstance(value, str):
        return True
