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

    A
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
    # ---NoOver---(Larger Even Above Even)
    # ---NoOver---(Larger Even Above Odd)
    # ---NoOver---(Larger Odd Above Even)
    # ---NoOver---(Larger Odd Above Odd)
    # ---NoOver---(Larger Even Above Even Equal Ends)
    # ---NoOver---(Larger Even Above Odd Equal Ends)
    # ---NoOver---(Larger Odd Above Even Equal Ends)
    # ---NoOver---(Larger Odd Above Odd Equal Ends)
    # ---NoOver---(Larger Even Above Even Equal Ins)
    # ---NoOver---(Larger Even Above Odd Equal Ins)
    # ---NoOver---(Larger Odd Above Even Equal Ins)
    # ---NoOver---(Larger Odd Above Odd Equal Ins)
    # ---NoOver---(Smaller Even Above Even)
    # ---NoOver---(Smaller Even Above Odd)
    # ---NoOver---(Smaller Odd Above Even)
    # ---NoOver---(Smaller Odd Above Odd)
    # ---NoOver---(Smaller Even Above Even Equal Ends)
    # ---NoOver---(Smaller Even Above Odd Equal Ends)
    # ---NoOver---(Smaller Odd Above Even Equal Ends)
    # ---NoOver---(Smaller Odd Above Odd Equal Ends)
    # ---NoOver---(Smaller Even Above Even Equal Ins)
    # ---NoOver---(Smaller Even Above Odd Equal Ins)
    # ---NoOver---(Smaller Odd Above Even Equal Ins)
    # ---NoOver---(Smaller Odd Above Odd Equal Ins)
    # ---NoOver---(Equal Even Above Even)
    # ---NoOver---(Equal Even Above Odd)
    # ---NoOver---(Equal Odd Above Even)
    # ---NoOver---(Equal Odd Above Odd)
    # ---NoOver---(Equal Even Above Even Equal Ends)
    # ---NoOver---(Equal Even Above Odd Equal Ends)
    # ---NoOver---(Equal Odd Above Even Equal Ends)
    # ---NoOver---(Equal Odd Above Odd Equal Ends)
    # ---NoOver---(Equal Even Above Even Equal Ins)
    # ---NoOver---(Equal Even Above Odd Equal Ins)
    # ---NoOver---(Equal Odd Above Even Equal Ins)
    # ---NoOver---(Equal Odd Above Odd Equal Ins)
    # ---NoOver---(Larger Even Above Tiny Even)
    # ---NoOver---(Larger Even Above Tiny Odd)
    # ---NoOver---(Larger Odd Above Tiny Even)
    # ---NoOver---(Larger Odd Above Tiny Odd)
    # ---NoOver---(Larger Even Above Tiny Even Equal Ends)
    # ---NoOver---(Larger Even Above Tiny Odd Equal Ends)
    # ---NoOver---(Larger Odd Above Tiny Even Equal Ends)
    # ---NoOver---(Larger Odd Above Tiny Odd Equal Ends)
    # ---NoOver---(Larger Even Above Tiny Even Equal Ins)
    # ---NoOver---(Larger Even Above Tiny Odd Equal Ins)
    # ---NoOver---(Larger Odd Above Tiny Even Equal Ins)
    # ---NoOver---(Larger Odd Above Tiny Odd Equal Ins)
    # ---NoOver---()

    # Overlapping Lists
    # ----Over----(Larger Even Above Even)
    # ----Over----(Larger Even Above Odd)
    # ----Over----(Larger Odd Above Even)
    # ----Over----(Larger Odd Above Odd)
    # ----Over----(Larger Even Above Even Equal Ends)
    # ----Over----(Larger Even Above Odd Equal Ends)
    # ----Over----(Larger Odd Above Even Equal Ends)
    # ----Over----(Larger Odd Above Odd Equal Ends)
    # ----Over----(Larger Even Above Even Equal Ins)
    # ----Over----(Larger Even Above Odd Equal Ins)
    # ----Over----(Larger Odd Above Even Equal Ins)
    # ----Over----(Larger Odd Above Odd Equal Ins)
    # ----Over----(Smaller Even Above Even)
    # ----Over----(Smaller Even Above Odd)
    # ----Over----(Smaller Odd Above Even)
    # ----Over----(Smaller Odd Above Odd)
    # ----Over----(Smaller Even Above Even Equal Ends)
    # ----Over----(Smaller Even Above Odd Equal Ends)
    # ----Over----(Smaller Odd Above Even Equal Ends)
    # ----Over----(Smaller Odd Above Odd Equal Ends)
    # ----Over----(Smaller Even Above Even Equal Ins)
    # ----Over----(Smaller Even Above Odd Equal Ins)
    # ----Over----(Smaller Odd Above Even Equal Ins)
    # ----Over----(Smaller Odd Above Odd Equal Ins)
    # ----Over----(Equal Even Above Even)
    # ----Over----(Equal Even Above Odd)
    # ----Over----(Equal Odd Above Even)
    # ----Over----(Equal Odd Above Odd)
    # ----Over----(Equal Even Above Even Equal Ends)
    # ----Over----(Equal Even Above Odd Equal Ends)
    # ----Over----(Equal Odd Above Even Equal Ends)
    # ----Over----(Equal Odd Above Odd Equal Ends)
    # ----Over----(Equal Even Above Even Equal Ins)
    # ----Over----(Equal Even Above Odd Equal Ins)
    # ----Over----(Equal Odd Above Even Equal Ins)
    # ----Over----(Equal Odd Above Odd Equal Ins)
    # ----Over----(Larger Even Above Tiny Even)
    # ----Over----(Larger Even Above Tiny Odd)
    # ----Over----(Larger Odd Above Tiny Even)
    # ----Over----(Larger Odd Above Tiny Odd)
    # ----Over----(Larger Even Above Tiny Even Equal Ends)
    # ----Over----(Larger Even Above Tiny Odd Equal Ends)
    # ----Over----(Larger Odd Above Tiny Even Equal Ends)
    # ----Over----(Larger Odd Above Tiny Odd Equal Ends)
    # ----Over----(Larger Even Above Tiny Even Equal Ins)
    # ----Over----(Larger Even Above Tiny Odd Equal Ins)
    # ----Over----(Larger Odd Above Tiny Even Equal Ins)
    # ----Over----(Larger Odd Above Tiny Odd Equal Ins)
    # ----Over----()
    def test_Over_1(self):
        l1 = [1,2,3]
        l2 = [4,5,6]
        v = median_eval(l1,l2)
        self.assertEqual(v, 3.5)

    def test_Over_1r(self):
        v = median_eval(l2,l1)
        self.assertEqual(v, 3.5)

    def test_Over_2(self):
        l1 = [1,2,3]
        l2 = [5,6,7]
        v = median_eval(l1,l2)
        self.assertEqual(v, 4.0)

    def test_Over_2r(self):
        v = median_eval(l2,l1)
        self.assertEqual(v, 4.0)

    #    (Different Sizes)
    def test_Over_3(self):
        l1 = [1,2,3]
        l2 = [5,6]
        v = median_eval(l1,l2)
        self.assertEqual(v, 3.0)

    def test_Over_3r(self):
        v = median_eval(l2,l1)
        self.assertEqual(v, 3.0)

    def test_Over_4(self):
        l1 = [1,2,3,4]
        l2 = [5,6]
        v = median_eval(l1,l2)
        self.assertEqual(v, 3.5)

    def test_Over_4r(self):
        v = median_eval(l2,l1)
        self.assertEqual(v, 3.5)

    def test_Over_5(self):
        l1 = [1,2,3,4,5]
        l2 = [6,7]
        v = median_eval(l1,l2)
        self.assertEqual(v, 4)

    def test_Over_5r(self):
        v = median_eval(l2,l1)
        self.assertEqual(v, 4)

    # Container Lists
    #    (Even Contains Odd)
    #    (Even Contains Even)
    #    (Odd Contains Odd)
    #    (Odd Contains Even)
    #    ()
    #    (Larger Even Above Even)
    #    (Larger Even Above Odd)
    #    (Larger Odd Above Even)
    #    (Larger Odd Above Odd)
    #    (Smaller Even Above Even)
    #    (Smaller Even Above Odd)
    #    (Smaller Odd Above Even)
    #    (Smaller Odd Above Odd)
    #    (Equal Even Above Even)
    #    (Equal Even Above Odd)
    #    (Equal Odd Above Even)
    #    (Equal Odd Above Odd)
    #    (Larger Even Above Tiny Even)
    #    (Larger Even Above Tiny Odd)
    #    (Larger Odd Above Tiny Even)
    #    (Larger Odd Above Tiny Odd)
    #    ()

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
