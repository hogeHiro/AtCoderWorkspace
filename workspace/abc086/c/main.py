#!/usr/bin/env python3

from typing import Tuple
from typing import List


Coordinate = Tuple[int, int, int]


def main():
    N = int(input())
    codList: List[Coordinate] = [(0, 0, 0)]
    for i in range(0, N):
        args = list(map(lambda x: int(x), input().split()))
        codList.append((args[0], args[1], args[2]))

    for i in range(1, N + 1):
        start = codList[i - 1]
        end = codList[i]
        dis = distance(start, end)
        duration = end[0] - start[0]

        if (duration - dis >= 0) and ((duration - dis) % 2 == 0):
            continue
        else:
            print("No")
            return

    print("Yes")


def distance(cod1: Coordinate, cod2: Coordinate):
    return abs(cod1[1] - cod2[1]) + abs(cod1[2] - cod2[2])


if __name__ == "__main__":
    main()
