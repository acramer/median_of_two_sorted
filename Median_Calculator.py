#!/usr/bin/env python3

# ----------
# Median_Calculator.py
# ----------

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# -------
# imports
# -------

from typing import IO, List

from sys import stdin, stdout

# ------------
# median_read
# ------------


def median_read(s: str) -> List[int]:
    a = s.split()
    return [int(b) for b in a]


# ------------
# median_eval
# ------------


def median_eval(i: List[int], j: List[int]) -> float:
    # Basic Version
    i = sorted(i+j)
    if len(i)%2 == 0:
        return (i[len(i)//2]+i[len(i)//2 - 1])/2.0 
    else:
        return i[len(i)//2]/1.0


def binaryMove(l: int, r:int) -> int:
    return -1


def median_print(w: IO[str], i: List[int], j: List[int], v: int) -> None:
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    i = " ".join(list(map(str, i)))
    j = " ".join(list(map(str, j)))
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")


# -------------
# median_solve
# -------------


def median_solve(r: IO[str], w: IO[str]) -> None:
    """
    r a reader
    w a writer
    """
    riter = iter(r)
    try:
        while True:
            s1, s2 = median_read(next(riter)), median_read(next(riter))
            v = median_eval(s1, s2)
            median_print(w, s1, s2, v)
    except StopIteration:
        pass

if __name__ == '__main__':
    median_solve(stdin, stdout)
