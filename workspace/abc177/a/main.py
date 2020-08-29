#!/usr/bin/env python3

# from typing import Optional
# from typing import List
# from typing import Dict
# from typing import Tuple
# from typing import Sequence


def main():
    args = input().split()
    D = int(args[0])
    T = int(args[1])
    S = int(args[2])

    time = D / S
    if T >= time:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
