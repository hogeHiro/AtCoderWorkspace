#!/usr/bin/env python3


def main():
    N = int(input())
    aList = list(map(lambda x: int(x), input().split()))

    aliceValue = 0
    bobValue = 0
    isAliceTurn = True
    while len(aList) > 0:
        maxValue = max(aList)
        aList.remove(maxValue)
        if isAliceTurn:
            aliceValue += maxValue
        else:
            bobValue += maxValue

        isAliceTurn = not isAliceTurn

    print(aliceValue - bobValue)


if __name__ == "__main__":
    main()
