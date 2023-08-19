def remove_last_item(lst: list) -> list:
    """Return list L with the last item removed

    Precondition: len(L) >= 0

    >>> remove_last_item([1, 2, 3, 4])
    [1, 2, 3]
    """
    # del lst[-1]
    lst.pop(-1)
    return lst


sp_girls = ["Madison", "Olivia", "Nicole", "Ally", "Ella", "Mei", "Jessica"]
remove_last_item(sp_girls)
print(sp_girls)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Could also test using command python -m doctest -v main.py
# Where the -m flag means run the doctest lib as a script
