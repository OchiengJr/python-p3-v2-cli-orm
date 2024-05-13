#!/usr/bin/env python3

def pytest_itemcollected(item):
    """
    Customizes the display of test item names in pytest.

    Args:
        item: The pytest test item being collected.
    """
    # Get the parent and node objects
    par = item.parent.obj if item.parent else None
    node = item.obj

    # Extract prefixes and suffixes
    pref = par.__doc__.strip() if par and par.__doc__ else par.__class__.__name__
    suf = node.__doc__.strip() if node and node.__doc__ else node.__name__

    # Combine prefixes and suffixes
    if pref or suf:
        item._nodeid = ' '.join((pref, suf))

