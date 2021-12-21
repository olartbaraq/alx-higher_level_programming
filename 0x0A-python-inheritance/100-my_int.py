#!/usr/bin/python3
""" defines a class """


class MyInt(int):
    """ a rebel : reverses operators == and !="""
    def __eq__(self, other):
        """Swaps meaning of `==` with `!=`
        Args:
            other: object to compare with `self`
        Returns: True if `self` and `other` *are not* equal,
            False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """Swaps meaning of `==` with `!=`
        Args:
            other: object to compare with `self`
        Returns: False if `self` and `other` *are not* equal,
            True otherwise.
        """
        return super().__eq__(other)
