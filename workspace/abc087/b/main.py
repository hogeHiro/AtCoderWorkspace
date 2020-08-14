#!/usr/bin/env python3

from typing import Tuple
from typing import Optional
from typing import List
from enum import Enum, auto

Result = Tuple[int, int, int]


class Coin(Enum):
    COIN_500 = auto()
    COIN_100 = auto()
    COIN_50 = auto()


def main():
    A = int(input())
    B = int(input())
    C = int(input())
    X = int(input())
    tempResult = minResult(X)
    if tempResult is None:
        print(0)
        return

    allResultList = set(parseResult(tempResult, Coin.COIN_500))
    resultList = list(
        filter(lambda x: x[0] <= A and x[1] <= B and x[2] <= C, allResultList)
    )
    print(len(resultList))


def minResult(value: int) -> Optional[Result]:
    remain = value
    minA = value // 500
    remain -= 500 * minA
    minB = remain // 100
    remain -= 100 * minB
    minC = remain // 50
    remain -= 50 * minC

    if remain == 0:
        return minA, minB, minC
    else:
        return None


def newResult(result: Result, target: Coin) -> Result:
    a, b, c = result
    if target == Coin.COIN_500:
        return a - 1, b + 5, c
    elif target == Coin.COIN_100:
        return a, b - 1, c + 2
    elif target == Coin.COIN_50:
        return result


def parseResult(result: Result, target: Coin) -> List[Result]:
    a, b, c = result
    resultList: List[Result] = []

    if target == Coin.COIN_500:
        resultList = resultList + parseResult(result, Coin.COIN_100)
        resultList = resultList + parseResult(result, Coin.COIN_50)
        if a > 0:
            new = newResult(result, target)
            resultList = resultList + parseResult(new, Coin.COIN_500)
            resultList = resultList + parseResult(new, Coin.COIN_100)
            resultList = resultList + parseResult(new, Coin.COIN_50)
    elif target == Coin.COIN_100:
        resultList = resultList + parseResult(result, Coin.COIN_50)
        if b > 0:
            new = newResult(result, target)
            resultList = resultList + parseResult(new, Coin.COIN_100)
            resultList = resultList + parseResult(new, Coin.COIN_50)
    elif target == Coin.COIN_50:
        resultList.append(result)

    return resultList


if __name__ == "__main__":
    main()
