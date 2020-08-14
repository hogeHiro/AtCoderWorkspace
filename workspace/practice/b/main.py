#!/usr/bin/env python3

from typing import List
import sys

LABEL_LIST = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

ANS = ["E", "G", "B", "C", "F", "A", "D"]

Q = 0

sys.setrecursionlimit(2000)


def main():
    global Q
    args = input().split()
    # args = "7 1000".split()
    N = int(args[0])
    Q = int(args[1])

    targetList = LABEL_LIST[:N]
    result = quickSort(targetList)
    print(f"! {''.join(result)}")


def quickSort(targetList: List[str]) -> List[str]:
    smaller: list[str] = []
    bigger: list[str] = []
    standard = targetList[0]

    if Q <= 0:
        return targetList

    if len(targetList) == 2:
        if diff(targetList[0], targetList[1]):
            return [targetList[1], targetList[0]]
        else:
            return targetList

    start = 0
    end = len(targetList) - 1
    while end > start:
        for i in list(range(start, end + 1)):
            start = i
            if diff(targetList[i], standard):
                break
            else:
                smaller.append(targetList[i])

        for i in reversed(list(range(start, end + 1))):
            end = i
            if diff(standard, targetList[i]):
                break
            else:
                if end > start:
                    bigger.insert(0, targetList[i])

        if end > start:
            smaller.append(targetList[end])
            bigger.insert(0, targetList[start])
            start += 1
            end -= 1

        if end <= start:
            if diff(targetList[start], standard):
                bigger.insert(0, targetList[start])
            else:
                smaller.append(targetList[start])

    if len(smaller) == 0 or len(bigger) == 0:
        return quickSort(targetList[1:] + targetList[:1])

    if len(smaller) > 1:
        smaller = quickSort(smaller)

    if len(bigger) > 1:
        bigger = quickSort(bigger)

    return smaller + bigger


# a のほうが大きいときに true, aのほうが小さいときに false
def diff(a: str, b: str) -> bool:
    global Q
    if Q <= 0:
        return True

    if a == b:
        return True
    Q -= 1
    print(f"? {a} {b}")
    result = input()
    return result == ">"
    # inA = ANS.index(a)
    # inB = ANS.index(b)
    # return inA > inB


if __name__ == "__main__":
    main()
