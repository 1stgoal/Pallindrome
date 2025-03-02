
# is_palindrome accepts str or else raise ValueError when not str
def is_palindrome(value: str) -> bool:
    if not isinstance(value, str):
        raise ValueError
    else:
        return True
