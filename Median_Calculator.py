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
    # Faster Version
    # Loop:
    while len(bucketOne) == 1 or len(bucketTwo) == 1:
    # 1. Divide Buckets in 2. Defaults to having larger half in the first half
        bucketOne = [bucketOne[(len(bucketOne)+1)//2], bucketOne[(len(bucketOne)+1)//2]]
        bucketTwo = [bucketTwo[(len(bucketTwo)+1)//2], bucketTwo[(len(bucketTwo)+1)//2]]
    # 2. Find interior edges that correspond to the 4 sub-buckets
        interiors = sorted(
                        list(
                            zip(
                                [bucketOne[0][-1], bucketOne[1][0] ,bucketTwo[0][-1], bucketTwo[1][0]],
                                range(4)))
                        , key=lambda x:x[0])

    # 3. Remove exterior sub-buckets
    #   *SEPARATE ALGORITHM*
    #   - Keep track of # removed from each super bucket
    # 4. Balence removals from each side using the side with the larger removal
    #   *SEPARATE ALGORITHM*
    #   a. if removal fails, break loop and follow base case (c)
    # 5. Check Base Cases
    #   a. [i][i]
    #   b. [ii][i]
    #   - If not in base case REPEAT
    #   c. Failed removal balance
    # Exit Loop
    # 6. Follow




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
