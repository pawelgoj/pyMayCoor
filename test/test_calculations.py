import pytest
from main.BondOrderCalculations.calculations import Histogram

from pprint import pprint


class TestHistogram:
    values = [2, 2.5, 3, 5, 6, 7, 6, 3, 3.75, 2.5]

    def test_calculate(self):

        result = Histogram.calculate(self.values, 3)
        assert (result.x == [2.8333333333333335, 4.5, 6.166666666666667]
                and result. y == [5, 2, 3])

    def test_to_string(self):

        string = Histogram.calculate(self.values, 3)\
            .to_string('P', 'O')

        assert string == ("P, O\n"
                          + "\n"
                          + "Interval/2 Count\n\n"
                          + "2.8333333333333335 5\n"
                          + "4.5 2\n"
                          + "6.166666666666667 3\n\n")
