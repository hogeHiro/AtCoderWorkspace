#!/usr/bin/env python3

from typing import List


def main():
    N = int(input())
    dList: List[int] = []
    for i in range(0, N):
        dList.append(int(input()))

    counter = 0
    while len(dList) > 0:
        maxValue = max(dList)
        dList = list(filter(lambda x: x < maxValue, dList))
        counter += 1

    print(counter)


if __name__ == "__main__":
    main()
