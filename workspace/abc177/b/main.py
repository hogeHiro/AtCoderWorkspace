#!/usr/bin/env python3

# from typing import Optional
# from typing import List
# from typing import Dict
# from typing import Tuple
# from typing import Sequence


def main():
    S = input()
    T = input()

    S_ary = list(S)
    T_ary = list(T)

    diff = len(S_ary) - len(T_ary) + 1
    tLen = len(T_ary)

    minCounter = 1000
    for i in range(diff):
        tempS = S_ary[i : i + tLen]

        counter = 0
        for charIndex in range(tLen):
            if tempS[charIndex] != T_ary[charIndex]:
                counter += 1
        minCounter = min(minCounter, counter)

    print(minCounter)


if __name__ == "__main__":
    main()
