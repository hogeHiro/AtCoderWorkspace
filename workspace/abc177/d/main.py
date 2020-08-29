#!/usr/bin/env python3

# from typing import Optional
# from typing import List
# from typing import Dict
# from typing import Tuple
# from typing import Sequence


def main():
    args = input().split()
    N = int(args[0])
    M = int(args[1])

    groupTable = [i for i in range(N + 1)]

    for i in range(M):
        args = list(map(lambda x: int(x), input().split()))
        if groupTable[args[0]] > groupTable[args[1]]:
            groupTable[args[0]] = groupTable[args[1]]
        else:
            groupTable[args[1]] = groupTable[args[0]]

    maxNum = 0
    for i in set(groupTable):
        counter = groupTable.count(i)
        maxNum = max(maxNum, counter)

    print(maxNum)


if __name__ == "__main__":
    main()

