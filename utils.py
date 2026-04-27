"""
utils.py

Helper functions used across the veterinary practice system.
"""


def find_by_name(name, items):
    """
    Search a list of objects and return the first item
    whose 'name' attribute matches the given name.

    Args:
        name (str): Name to search for
        items (list): List of objects that have a 'name' attribute

    Returns:
        object or None: The matching item if found, otherwise None
    """
    for item in items:
        if item.name == name:
            return item

    return None