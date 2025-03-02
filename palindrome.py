""" is_palindrome detects if a string is palindrome """

from collections import deque


def is_palindrome(value: str) -> bool:
    if not isinstance(value, str):
        raise ValueError
    elif not value:
        return False
    elif isinstance(value, str):
        # converting the value variable to deque and dek_value.reverse() reverses the string.
        dek_value = deque(value)
        dek_value.reverse()

        # converting the deque to list, then using map before joining into string.
        my_list = []
        for i in dek_value:
            my_list.append(i)
        palindrome_string = map(str, my_list)
        result = ''.join(palindrome_string)

        # converting both the strings to lowercase and comparing original string with the reversed string.
        if result.lower() == value.lower():
            return True
        else:
            return False
