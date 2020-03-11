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
    """
    return basicMedian(i,j)
    """
    return advancedMedian(i,j)

def basicMedian(i: List[int], j: List[int]) -> float:
    """
    Basic Version
    """
    i = sorted(i+j)
    if len(i)%2 == 0:
        return (i[len(i)//2]+i[len(i)//2 - 1])/2.0 
    else:
        return i[len(i)//2]/1.0

def advancedMedian(i: List[int], j: List[int]) -> float:
    # Debug
    # print("\n\ni:", i, "\nj:", j)
    """
    Faster Version
    - len(i) = n, len(j) = m
    - Supposedly log(n+m)
    """
    bucketOne, bucketTwo = i[:], j[:]
    while True:
        # Debug
        print('     bucketOne:',bucketOne)
        print('     bucketTwo:',bucketTwo)

        # Fix lists that can't split
        if   len(bucketOne) == 1 and len(bucketTwo) > 2:
            bucketOne = sorted(bucketOne+bucketTwo[-1:])
            bucketTwo = bucketTwo[:-1]
        elif len(bucketTwo) == 1 and len(bucketOne) > 2:
            bucketTwo = sorted(bucketTwo+bucketOne[-1:])
            bucketOne = bucketOne[:-1]

        # Debug
        print('     -> bucketOne:',bucketOne)
        print('     -> bucketTwo:',bucketTwo)

        # Base Case: Check to see if we can combine the lists
        if len(bucketOne) == 0 or len(bucketTwo) == 0 or bucketOne[-1] <= bucketTwo[0] or bucketTwo[-1] <= bucketOne[0]:
            if len(bucketTwo) == 0:
                combine = bucketOne
            elif len(bucketOne) == 0:
                combine = bucketTwo
            elif bucketOne[-1] <= bucketTwo[0]:
                combine = bucketOne+bucketTwo
            elif bucketTwo[-1] <= bucketOne[0]:
                combine = bucketTwo+bucketOne
            # Median calc
            if len(combine) % 2 == 0:
                return sum(combine[(len(combine)-1)//2:len(combine)//2+1])/2.0
            else:
                return combine[(len(combine)-1)//2]/1.0

        # 0. Check Base Cases
        if   len(bucketOne) == 1 and len(bucketTwo) == 1:
            return (bucketOne[0]+bucketTwo[0])/2.0
        elif {len(bucketOne),len(bucketTwo)} == {1,2}:
            return sorted(bucketOne+bucketTwo)[1]/1.0

        # 1. Create super buckets by creating 2 evenly distributed sub buckets.
        # - Defaults to having larger half in the first half
        b1 = [bucketOne[:(len(bucketOne)+1)//2], bucketOne[(len(bucketOne)+1)//2:]]
        b2 = [bucketTwo[:(len(bucketTwo)+1)//2], bucketTwo[(len(bucketTwo)+1)//2:]]

        # Debug
        print("b1:",b1)
        print("b2:",b2)

        # 2. Remove exterior sub-buckets
        # Find interior edges that correspond to the 4 sub-buckets and find the edge sub-buckets
        pruned = sorted(list(zip([b1[0][-1], b1[1][0], b2[0][-1], b2[1][0]], range(4))), key=lambda x:x[0])
        # Select sub-buckets to prune
        pruned = [pruned[0][1], pruned[-1][1]]
        # Base Case: If pruned are both from the same super bucket
        # Reset buckets and continue
        if set(pruned) == {0,1}:
            toAdd = []
            if len(b1[pruned[0]]) != len(b1[pruned[1]]):
                toAdd = b1[pruned[0]][-1:]
                bucketOne = toAdd + b2[0] if toAdd[0] < b2[0][-1] else b2[0] + toAdd
            else:
                bucketOne = b2[0]
            bucketTwo = b2[1]
            continue
        elif set(pruned) == {2,3}:
            toAdd = []
            if len(b2[pruned[0]-2]) != len(b2[pruned[1]-2]):
                toAdd = b2[pruned[0]-2][-1:]
                bucketOne = toAdd + b1[0] if toAdd[0] < b1[0][-1] else b1[0] + toAdd
            else:
                bucketOne = b1[0]
            bucketTwo = b1[1]
            continue

        # 3. Find which bucket pruned a larger bucket
        # Find the difference in bucket removal 
        intb1, extb1 = (1,0) if 0 in pruned else (0,1)
        intb2, extb2 = (1,0) if 2 in pruned else (0,1)
        if len(b1[extb1]) > len(b2[extb2]):
            largerExt  = b1[extb1]
            largerInt  = b1[intb1]
            smallerExt = b2[extb2]
            smallerInt = b2[intb2]
            # Pick side
            side = intb1
        else:
            largerExt  = b2[extb2]
            largerInt  = b2[intb2]
            smallerExt = b1[extb1]
            smallerInt = b1[intb1]
            # Pick side
            side = intb2
        # Debug
        print("largerExt ", largerExt )
        print("largerInt ", largerInt )
        print("smallerExt", smallerExt)
        print("smallerInt", smallerInt)
        print("side      ", side      )

        # 4. Find the ammount to balance the larger interior bucket
        toRemove = len(largerExt) - len(smallerExt) 
        # print("     toRemove  :",toRemove  )

        # 5. If removal fails, break loop and follow base case (c)
        if toRemove >= len(largerInt):
            # Debug
            print("     largerExt :",largerExt )
            print("     largerInt :",largerInt )
            print("     smallerExt:",smallerExt)
            print("     smallerInt:",smallerInt)
            print("     side      :",side      )
            print("     toRemove  :",toRemove  )
            assert toRemove <= len(largerInt)
            assert len(smallerInt) <= 2
            combine = sorted(largerExt[-1:]+smallerInt+largerInt[:1])
            print("     Combine  :",combine  )
            # Median calc
            if len(combine) % 2 == 0:
                return sum(combine[(len(combine)-1)//2:len(combine)//2+1])/2.0
            else:
                return combine[(len(combine)-1)//2]/1.0

        # 6. Remove the difference from the exterior of the remaining sub-bucket of the bucket with the larger pruned sub-bucket
        # # Debug
        # print('     Side:', side)
        if side == 0:
            largerInt = largerInt[toRemove:]
        else:
            largerInt = largerInt[:len(largerInt) - toRemove]

        # 7. Populate the buckets with the remaining buckets
        bucketOne = largerInt
        bucketTwo = smallerInt

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
