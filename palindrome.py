def is_palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome

    :param value: A s                               tring
    :return: A boolean
    """
    pal = ''.join(char.lower() for char in value if char.isalnum())
    return pal == pal[::-1]  # remove pass statement and implement me
