#!/usr/bin/env python3
"""Type checking"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    """
    Zoom in on the elements of a tuple by repeating each element.

    Args:
        lst (Tuple): The input tuple.
        factor (int, optional): The factor by which each element
        should be repeated. Defaults to 2.

    Returns:
        Tuple: The resulting tuple after zooming in.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return tuple(zoomed_in)


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
