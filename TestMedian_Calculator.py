#!/usr/bin/env python3

# --------------
# TestMedian_Calculator.py
# --------------

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Median_Calculator import median_read, median_eval, median_print, median_solve

# -----------
# TestMedian_Calculator
# -----------


class TestMedian_Calculator(TestCase):
    # ----
    # read
    # ----

    def test_read(self):
        s = "1 10\n"
        i = median_read(s)
        self.assertEqual(i, [1, 10])

    # ----
    # eval
    # ----

    # Basic tests
    def test_Basic_1(self):
        l1 = [1, 10]
        l2 = [100, 200]
        v = median_eval(l1,l2)
        self.assertEqual(v, 55)

    def test_Basic_1r(self):
        l1 = [1, 10]
        l2 = [100, 200]
        v = median_eval(l2,l1)
        self.assertEqual(v, 55)

    def test_Basic_2(self):
        l1 = list(range(110, 211))
        l2 = list(range(900, 1102, 2))
        v = median_eval(l1,l2)
        self.assertEqual(v, 555)

    def test_Basic_2r(self):
        l1 = list(range(110, 211))
        l2 = list(range(900, 1102, 2))
        v = median_eval(l2,l1)
        self.assertEqual(v, 555)

    # Non-Overlapping Lists
    #    (Same Sizes)
    def test_NoOver_1(self):
        l1 = [1,2,3]
        l2 = [4,5,6]
        v = median_eval(l1,l2)
        self.assertEqual(v, 3.5)

    def test_NoOver_1r(self):
        l1 = [1,2,3]
        l2 = [4,5,6]
        v = median_eval(l2,l1)
        self.assertEqual(v, 3.5)

    def test_NoOver_2(self):
        l1 = [1,2,3]
        l2 = [5,6,7]
        v = median_eval(l1,l2)
        self.assertEqual(v, 4.0)

    def test_NoOver_2r(self):
        l1 = [1,2,3]
        l2 = [5,6,7]
        v = median_eval(l2,l1)
        self.assertEqual(v, 4.0)

    #    (Different Sizes)
    def test_NoOver_3(self):
        l1 = [1,2,3]
        l2 = [5,6]
        v = median_eval(l1,l2)
        self.assertEqual(v, 3.0)

    def test_NoOver_3r(self):
        l1 = [1,2,3]
        l2 = [5,6]
        v = median_eval(l2,l1)
        self.assertEqual(v, 3.0)

    def test_NoOver_4(self):
        l1 = [1,2,3,4]
        l2 = [5,6]
        v = median_eval(l1,l2)
        self.assertEqual(v, 3.5)

    def test_NoOver_4r(self):
        l1 = [1,2,3,4]
        l2 = [5,6]
        v = median_eval(l2,l1)
        self.assertEqual(v, 3.5)

    def test_NoOver_5(self):
        l1 = [1,2,3,4,5]
        l2 = [6,7]
        v = median_eval(l1,l2)
        self.assertEqual(v, 4)

    def test_NoOver_5r(self):
        l1 = [1,2,3,4,5]
        l2 = [6,7]
        v = median_eval(l2,l1)
        self.assertEqual(v, 4)

    # Overlapping Lists

    # Container Lists

    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        median_print(w, [1], [10], 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        median_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 100 200 55.0\n201 210 900 1000 555.0\n"
        )


# ----
# main
# ----

if __name__ == "__main__":  # pragma: no cover
    main()
