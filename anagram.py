def is_anagram(first_string: str, second_string: str) -> bool:
    """
    Given two strings, this functions determines if they are an anagram of one another.
    """
    one_string = sorted(first_string)
    two_string = sorted(second_string)

    if (one_string == two_string):
        return True
    else:
        return False


