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

    groupList = list()
    for i in range(M):
        args = list(map(lambda x: int(x), input().split()))

        isHit = False
        for group in groupList:
            if args[0] in group:
                group.add(args[1])
                isHit = True
            elif args[1] in group:
                group.add(args[0])
                isHit = True

        if not isHit:
            groupList.append({args[0], args[1]})

    maxNum = 0
    for group in groupList:
        maxNum = max(maxNum, len(group))

    print(maxNum)


if __name__ == "__main__":
    main()
