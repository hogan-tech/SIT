# Author: Hogan Lin
# Date: Feb 6th, 2025
# Github: https://github.com/hogan-tech/SIT/tree/main/PythonIntro
# Description: Flattening arbitrarily nested lists.

def flatten(lst):
    """
    Recursively flattens an arbitrarily nested list.

    :param lst: A nested list
    :return: A flattened list containing all non-list elements
    """
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


