import numpy as np
from typing import Callable


class Histogram:
    """Methods to generate histograms"""
    histogram: Callable = np.histogram
    x: list[float] = []
    y: list[int] = []

    @classmethod
    def calculate_histogram(cls, values: list[float], bins: int)\
            -> tuple[list[float], list[int]]:
        """Calculate histogram.

        Args:
            values (list[float]): list of values
            bins (int): number of bins in histogram

        Returns:
            tuple[list[float], list[int]]: (list of x, list of y)
        """
        histogram = cls.histogram(values, bins)

        y = histogram[0]
        x = histogram[1]
        y = y.tolist()
        x = x.tolist()

        first_loop = True
        new_x = []
        for item in x:
            if first_loop:
                first_loop = False
                previous = item
            else:
                new_x.append((item
                              + previous) / 2)
                previous = item

        histogram = Histogram()
        histogram.x = new_x
        histogram.y = y
        return histogram

    def to_string(self, atom_symbol_1: str, atom_symbol_2: str)\
            -> str:
        string = atom_symbol_1 + ', ' + atom_symbol_2 + '\n\n'
        string = string + 'Interval/2' + ' ' + 'Count' + '\n\n'
        for i in range(len(self.x)):
            string = string + str(self.x[i]) + ' ' + str(self.y[i]) + '\n'

        string = string + '\n'

        return string
