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
        m = 55.0
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)

    def test_Basic_2(self):
        l1 = list(range(110, 211))
        l2 = list(range(900, 1102, 2))
        m = 555.0
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)
    # Edge tests
    def test_Edge_1(self):
        l1 = [13]
        l2 = []
        m = 13.0
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)

    def test_Edge_2(self):
        l1 = [5]
        l2 = [5]
        m = 5.0
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)

    def test_Edge_3(self):
        l1 = [9]
        l2 = [10]
        m = 9.5
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)

    def test_Edge_4(self):
        l1 = [9,11]
        l2 = []
        m = 10.0
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)

    def test_Edge_5(self):
        l1 = [9,11]
        l2 = [10]
        m = 10.0
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)

    def test_Edge_6(self):
        l1 = [9,11]
        l2 = [10,12]
        m = 10.5
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)

    def test_Edge_7(self):
        l1 = [1,2,3,4,5,6,7,8]
        l2 = []
        m = 4.5
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
                v = median_eval(*l[1])
                self.assertEqual(v, m)

    def test_Edge_8(self):
        l1 = [1,2,3,4,5,6,7]
        l2 = []
        m = 4.0
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)

    def test_Edge_9(self):
        l1 = [1,2,3,4,5,6,7,8]
        l2 = [5]
        m = 5.0
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)

    def test_Edge_10(self):
        l1 = [1,2,3,4,5,6,7]
        l2 = [4]
        m = 4.0
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)

    def test_Edge_11(self):
        l1 = []
        l2 = []
        m = None
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)

    # Non-Overlapping Lists
    # ---NoOver---(Larger Even Above Even)
    def test_NoOver_1(self):
        l1 = [1,2,3,4]
        l2 = [5,6]
        m = 3.5
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)
    # ---NoOver---(Larger Even Above Odd)
    def test_NoOver_2(self):
        l1 = [5,6,7,8]
        l2 = [2,3,4]
        m = 5.0
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)
    # ---NoOver---(Larger Odd Above Even)
    def test_NoOver_3(self):
        l1 = [5,6,7,8,9]
        l2 = [1,2,3,4]
        m = 5.0
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)
    # ---NoOver---(Larger Odd Above Odd)
    def test_NoOver_4(self):
        l1 = [4,5,6,7,8]
        l2 = [1,2,3]
        m = 4.5
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)
    # ---NoOver---(Larger Even Above Even Equal Ends)
    def test_NoOver_5(self):
        l1 = [4,5,6,7,8,9,10,11]
        l2 = [1,2,3,4]
        m = 5.5
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)
    # ---NoOver---(Larger Even Above Odd Equal Ends)
    def test_NoOver_6(self):
        l1 = [3,4,5,6,7,8,9,10]
        l2 = [1,2,3]
        m = 5.0
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)
    # ---NoOver---(Larger Odd Above Even Equal Ends)
    def test_NoOver_7(self):
        l1 = [4,5,6,7,8,9,10]
        l2 = [1,2,3,4]
        m = 5.0
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)
    # ---NoOver---(Larger Odd Above Odd Equal Ends)
    def test_NoOver_8(self):
        l1 = [3,4,5,6,7,8,9]
        l2 = [1,2,3]
        m = 4.5
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)
    # ---NoOver---(Larger Even Above Even Equal Ins)
    def test_NoOver_9(self):
        l1 = [4,4,6,7,8,9]
        l2 = [1,2,3,4]
        m = 4.0
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)
    # ---NoOver---(Larger Even Above Odd Equal Ins)
    def test_NoOver_10(self):
        l1 = [3,4,5,6]
        l2 = [1,2,3]
        m = 3.0
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)
    # ---NoOver---(Larger Odd Above Even Equal Ins)
    def test_NoOver_11(self):
        l1 = [4,5,6,7,8]
        l2 = [1,2,3,4]
        m = 4.0
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)
    # ---NoOver---(Larger Odd Above Odd Equal Ins)
    def test_NoOver_12(self):
        l1 = [3,3,3,6,7]
        l2 = [1,2,3]
        m = 3.0
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)
    # ---NoOver---(Equal Even Above Even)
    def test_NoOver_13(self):
        l1 = [5,6,7,8]
        l2 = [1,2,3,4]
        m = 4.5
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)
    # ---NoOver---(Equal Odd Above Odd)
    def test_NoOver_14(self):
        l1 = [6,7,8,9,10]
        l2 = [1,2,3,4,5]
        m = 5.5
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)
    # ---NoOver---(Equal Even Above Even Equal Ends)
    def test_NoOver_15(self):
        l1 = [4,5,6,7]
        l2 = [1,2,3,4]
        m = 4.0
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)
    # ---NoOver---(Equal Odd Above Odd Equal Ends)
    def test_NoOver_16(self):
        l1 = [5,6,7,8,9]
        l2 = [1,2,3,4,5]
        m = 5.0
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)
    # ---NoOver---(Larger Even Above Tiny Even)
    def test_NoOver_17(self):
        l1 = [3,4,5,6,7,8,9,10]
        l2 = [1,2]
        m = 5.5
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)
    # ---NoOver---(Larger Even Above Tiny Odd)
    def test_NoOver_18(self):
        l1 = [4,5,6,7,8,9,10,11]
        l2 = [1,2,3]
        m = 6.0
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)
    # ---NoOver---(Larger Odd Above Tiny Even)
    def test_NoOver_19(self):
        l1 = [3,4,5,6,7,8,9]
        l2 = [1,2]
        m = 5.0
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)
    # ---NoOver---(Larger Odd Above Tiny Odd)
    def test_NoOver_20(self):
        l1 = [4,5,6,7,8,9,10,11,12]
        l2 = [1,2,3]
        m = 6.5
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)
    # ---NoOver---(Larger Even Above Tiny Even Equal Ends)
    def test_NoOver_21(self):
        l1 = [2,3,4,5,6,7,8,9]
        l2 = [1,2]
        m = 4.5
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)
    # ---NoOver---(Larger Even Above Tiny Odd Equal Ends)
    def test_NoOver_22(self):
        l1 = [3,4,5,6,7,8,9,10]
        l2 = [1,2,3]
        m = 5.0
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)
    # ---NoOver---(Larger Odd Above Tiny Even Equal Ends)
    def test_NoOver_23(self):
        l1 = [2,3,4,5,6,7,8]
        l2 = [1,2]
        m = 4.0
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)
    # ---NoOver---(Larger Odd Above Tiny Odd Equal Ends)
    def test_NoOver_24(self):
        l1 = [3,4,5,6,7,8,9]
        l2 = [1,2,3]
        m = False
        assert False
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)


    # Overlapping Lists
    # ----Over----(Larger Even Above Even)
    def test_Over_1(self):
        l1 = [3,4,5,6,10,12]
        l2 = [1,4,8,9]
        m = False
        assert False
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)
    # ----Over----(Larger Even Above Odd)
    def test_Over_2(self):
        l1 = [3,4,5,6,10,12]
        l2 = [1,4,9]
        m = False
        assert False
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)
    # ----Over----(Larger Odd Above Even)
    def test_Over_3(self):
        l1 = [3,4,5,6,10,12,13]
        l2 = [1,4,8,9]
        m = False
        assert False
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)
    # ----Over----(Larger Odd Above Odd)
    def test_Over_4(self):
        l1 = [3,4,5,6,10,12,13]
        l2 = [1,4,9]
        m = False
        assert False
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)
    # ----Over----(Larger Even Above Even Equal Ends)
    def test_Over_5(self):
        l1 = [1,3,5,6,10,12,13]
        l2 = [1,4,9]
        m = False
        assert False
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)
    def test_Over_6(self):
        l1 = [3,4,5,6,10,12,13]
        l2 = [8,9,13]
        m = False
        assert False
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)
    # ----Over----(Larger Even Above Odd Equal Ends)
    def test_Over_7(self):
        l1 = [3,4,5,6,10,12,13]
        l2 = [5,8,9,13]
        m = False
        assert False
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)
    def test_Over_8(self):
        l1 = [1,4,5,6,10,12,13]
        l2 = [1,3,5,8]
        m = False
        assert False
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)
    # ----Over----(Larger Odd Above Even Equal Ends)
    def test_Over_9(self):
        l1 = [3,4,5,6,10,12,13,14]
        l2 = [5,8,9,14]
        m = False
        assert False
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)
    def test_Over_10(self):
        l1 = [1,4,5,6,10,12,13,14]
        l2 = [1,3,5,8]
        m = False
        assert False
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)
    # ----Over----(Larger Odd Above Odd Equal Ends)
    def test_Over_11(self):
        l1 = [3,4,5,6,10,12,13,14]
        l2 = [5,7,8,9,14]
        m = False
        assert False
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)
    def test_Over_12(self):
        l1 = [1,4,5,6,10,12,13,14]
        l2 = [1,3,5,8,9]
        m = False
        assert False
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)
    # ----Over----(Larger Even Above Even Equal Ins)
    def test_Over_13(self):
        l1 = [3,4,5,6,10,12,13,14]
        l2 = [5,7,8,9,14]
        m = False
        assert False
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)
    def test_Over_14(self):
        l1 = [1,4,5,6,10,12,13,14]
        l2 = [1,3,5,8,9]
        m = False
        assert False
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)
    # ----Over----(Larger Even Above Odd Equal Ins)
    def test_Over_n(self):
        l1 = []
        l2 = []
        m = False
        assert False
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)
    # ----Over----(Larger Odd Above Even Equal Ins)
    def test_Over_n(self):
        l1 = []
        l2 = []
        m = False
        assert False
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)
    # ----Over----(Larger Odd Above Odd Equal Ins)
    def test_Over_n(self):
        l1 = []
        l2 = []
        m = False
        assert False
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)
    # ----Over----(Equal Even Above Even)
    def test_Over_n(self):
        l1 = []
        l2 = []
        m = False
        assert False
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)
    # ----Over----(Equal Odd Above Odd)
    def test_Over_n(self):
        l1 = []
        l2 = []
        m = False
        assert False
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)
    # ----Over----(Equal Even Above Even Equal Ends)
    def test_Over_n(self):
        l1 = []
        l2 = []
        m = False
        assert False
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, m)
    # ----Over----(Equal Odd Above Odd Equal Ends)
    # ----Over----(Equal Even Above Even Equal Ins)
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


    # Container Lists
    # --Contains--(Even Contains Odd)
    # --Contains--(Even Contains Even)
    # --Contains--(Odd Contains Odd)
    # --Contains--(Odd Contains Even)
    # --Contains--(Larger Even Above Even)
    # --Contains--(Larger Even Above Odd)
    # --Contains--(Larger Odd Above Even)
    # --Contains--(Larger Odd Above Odd)
    # --Contains--(Smaller Even Above Even)
    # --Contains--(Smaller Even Above Odd)
    # --Contains--(Smaller Odd Above Even)
    # --Contains--(Smaller Odd Above Odd)
    # --Contains--(Equal Even Above Even)
    # --Contains--(Equal Even Above Odd)
    # --Contains--(Equal Odd Above Even)
    # --Contains--(Equal Odd Above Odd)
    # --Contains--(Larger Even Above Tiny Even)
    # --Contains--(Larger Even Above Tiny Odd)
    # --Contains--(Larger Odd Above Tiny Even)
    # --Contains--(Larger Odd Above Tiny Odd)

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
