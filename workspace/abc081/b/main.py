#!/usr/bin/env python3

from typing import List


def main():
    N = int(input())
    args = list(map(lambda x: int(x), input().split()))
    counter = 0
    target = args
    while canDev(target):
        counter += 1
        target = dev2(target)

    print(counter)


def canDev(target: List[int]) -> bool:
    for item in target:
        if item % 2 != 0:
            return False
    return True


def dev2(target: List[int]) -> List[int]:
    return list(map(lambda x: int(x / 2), target))


if __name__ == "__main__":
    main()
