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
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, 55.0)

    def test_Basic_2(self):
        l1 = list(range(110, 211))
        l2 = list(range(900, 1102, 2))
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, 555.0)

    # Edge tests
    def test_Edge_1(self):
        l1 = [13]
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, 13.0)

    def test_Edge_2(self):
        l1 = [5]
        l2 = [5]
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, 13.0)

    def test_Edge_3(self):
        l1 = [9]
        l2 = [10]
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, 9.5)

    def test_Edge_4(self):
        l1 = [9,11]
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, 10.0)

    def test_Edge_5(self):
        l1 = [9,11]
        l2 = [10]
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, 10.0)

    def test_Edge_6(self):
        l1 = [9,11]
        l2 = [10,12]
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, 10.0)

    def test_Edge_7(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, None)

    # Non-Overlapping Lists
    # ---NoOver---(Larger Even Above Even)
    def test_NoOver_1(self):
        l1 = [1,2,3,4]
        l2 = [5,6]
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, 3.5)

    # ---NoOver---(Larger Even Above Odd)
    def test_NoOver_2(self):
        l1 = [5,6,7,8]
        l2 = [2,3,4]
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ---NoOver---(Larger Odd Above Even)
    def test_NoOver_3(self):
        l1 = [5,6,7,8,9]
        l2 = [1,2,3,4]
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ---NoOver---(Larger Odd Above Odd)
    def test_NoOver_4(self):
        l1 = [4,5,6,7,8]
        l2 = [1,2,3]
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ---NoOver---(Larger Even Above Even Equal Ends)
    def test_NoOver_5(self):
        l1 = [4,5,6,7,8,9,10,11]
        l2 = [1,2,3,4]
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ---NoOver---(Larger Even Above Odd Equal Ends)
    def test_NoOver_6(self):
        l1 = [3,4,5,6,7,8,9,10]
        l2 = [1,2,3]
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ---NoOver---(Larger Odd Above Even Equal Ends)
    def test_NoOver_7(self):
        l1 = [4,5,6,7,8,9,10]
        l2 = [1,2,3,4]
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ---NoOver---(Larger Odd Above Odd Equal Ends)
    def test_NoOver_8(self):
        l1 = [3,4,5,6,7]
        l2 = [1,2,3]
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ---NoOver---(Larger Even Above Even Equal Ins)
    def test_NoOver_9(self):
        l1 = [4,5,6,7,8,9]
        l2 = [1,2,3,4]
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ---NoOver---(Larger Even Above Odd Equal Ins)
    def test_NoOver_10(self):
        l1 = [3,4,5,6]
        l2 = [1,2,3]
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ---NoOver---(Larger Odd Above Even Equal Ins)
    def test_NoOver_11(self):
        l1 = [4,5,6,7,8]
        l2 = [1,2,3,4]
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ---NoOver---(Larger Odd Above Odd Equal Ins)
    def test_NoOver_12(self):
        l1 = [3,4,5,6,7]
        l2 = [1,2,3]
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ---NoOver---(Smaller Even Above Even)
    def test_NoOver_13(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ---NoOver---(Smaller Even Above Odd)
    def test_NoOver_14(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ---NoOver---(Smaller Odd Above Even)
    def test_NoOver_15(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ---NoOver---(Smaller Odd Above Odd)
    def test_NoOver_16(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ---NoOver---(Smaller Even Above Even Equal Ends)
    def test_NoOver_17(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ---NoOver---(Smaller Even Above Odd Equal Ends)
    def test_NoOver_18(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ---NoOver---(Smaller Odd Above Even Equal Ends)
    def test_NoOver_19(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ---NoOver---(Smaller Odd Above Odd Equal Ends)
    def test_NoOver_20(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ---NoOver---(Smaller Even Above Even Equal Ins)
    def test_NoOver_21(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ---NoOver---(Smaller Even Above Odd Equal Ins)
    def test_NoOver_22(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ---NoOver---(Smaller Odd Above Even Equal Ins)
    def test_NoOver_23(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ---NoOver---(Smaller Odd Above Odd Equal Ins)
    def test_NoOver_24(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ---NoOver---(Equal Even Above Even)
    def test_NoOver_25(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ---NoOver---(Equal Even Above Odd)
    def test_NoOver_26(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ---NoOver---(Equal Odd Above Even)
    def test_NoOver_27(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ---NoOver---(Equal Odd Above Odd)
    def test_NoOver_28(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ---NoOver---(Equal Even Above Even Equal Ends)
    def test_NoOver_29(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ---NoOver---(Equal Even Above Odd Equal Ends)
    def test_NoOver_30(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ---NoOver---(Equal Odd Above Even Equal Ends)
    def test_NoOver_31(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ---NoOver---(Equal Odd Above Odd Equal Ends)
    def test_NoOver_32(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ---NoOver---(Equal Even Above Even Equal Ins)
    def test_NoOver_33(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ---NoOver---(Equal Even Above Odd Equal Ins)
    def test_NoOver_34(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ---NoOver---(Equal Odd Above Even Equal Ins)
    def test_NoOver_35(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ---NoOver---(Equal Odd Above Odd Equal Ins)
    def test_NoOver_36(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ---NoOver---(Larger Even Above Tiny Even)
    def test_NoOver_37(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ---NoOver---(Larger Even Above Tiny Odd)
    def test_NoOver_38(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ---NoOver---(Larger Odd Above Tiny Even)
    def test_NoOver_38(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ---NoOver---(Larger Odd Above Tiny Odd)
    def test_NoOver_39(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ---NoOver---(Larger Even Above Tiny Even Equal Ends)
    def test_NoOver_40(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ---NoOver---(Larger Even Above Tiny Odd Equal Ends)
    def test_NoOver_41(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ---NoOver---(Larger Odd Above Tiny Even Equal Ends)
    def test_NoOver_42(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ---NoOver---(Larger Odd Above Tiny Odd Equal Ends)
    def test_NoOver_43(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ---NoOver---(Larger Even Above Tiny Even Equal Ins)
    def test_NoOver_44(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ---NoOver---(Larger Even Above Tiny Odd Equal Ins)
    def test_NoOver_45(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ---NoOver---(Larger Odd Above Tiny Even Equal Ins)
    def test_NoOver_46(self):
        l1 = [2,3,4,5,6]
        l2 = [1,2]
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, 3.0)

    # ---NoOver---(Larger Odd Above Tiny Odd Equal Ins)
    def test_NoOver_47(self):
        l1 = [3,4,5,6,7]
        l2 = [1,2,3]
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, 4.0)

    # ---NoOver---()

    # Overlapping Lists
    # ----Over----(Larger Even Above Even)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Larger Even Above Odd)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Larger Odd Above Even)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Larger Odd Above Odd)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Larger Even Above Even Equal Ends)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Larger Even Above Odd Equal Ends)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Larger Odd Above Even Equal Ends)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Larger Odd Above Odd Equal Ends)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Larger Even Above Even Equal Ins)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Larger Even Above Odd Equal Ins)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Larger Odd Above Even Equal Ins)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Larger Odd Above Odd Equal Ins)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Smaller Even Above Even)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Smaller Even Above Odd)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Smaller Odd Above Even)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Smaller Odd Above Odd)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Smaller Even Above Even Equal Ends)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Smaller Even Above Odd Equal Ends)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Smaller Odd Above Even Equal Ends)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Smaller Odd Above Odd Equal Ends)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Smaller Even Above Even Equal Ins)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Smaller Even Above Odd Equal Ins)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Smaller Odd Above Even Equal Ins)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Smaller Odd Above Odd Equal Ins)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Equal Even Above Even)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Equal Even Above Odd)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Equal Odd Above Even)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Equal Odd Above Odd)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Equal Even Above Even Equal Ends)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Equal Even Above Odd Equal Ends)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Equal Odd Above Even Equal Ends)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Equal Odd Above Odd Equal Ends)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Equal Even Above Even Equal Ins)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Equal Even Above Odd Equal Ins)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Equal Odd Above Even Equal Ins)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Equal Odd Above Odd Equal Ins)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Larger Even Above Tiny Even)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Larger Even Above Tiny Odd)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Larger Odd Above Tiny Even)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Larger Odd Above Tiny Odd)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Larger Even Above Tiny Even Equal Ends)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Larger Even Above Tiny Odd Equal Ends)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Larger Odd Above Tiny Even Equal Ends)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Larger Odd Above Tiny Odd Equal Ends)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Larger Even Above Tiny Even Equal Ins)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Larger Even Above Tiny Odd Equal Ins)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Larger Odd Above Tiny Even Equal Ins)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )

    # ----Over----(Larger Odd Above Tiny Odd Equal Ins)
    def test_Over_12(self):
        l1 = []
        l2 = []
        for l in [("Regular", (l1,l2)),("Fliped", (l2,l1))]
            with self.subTest(msg=l[0])
                v = median_eval(*l[1])
                self.assertEqual(v, )


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
