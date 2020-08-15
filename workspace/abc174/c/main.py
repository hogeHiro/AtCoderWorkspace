#!/usr/bin/env python3

# from typing import Optional
# from typing import List
# from typing import Dict
# from typing import Tuple
# from typing import Sequence


def main():
    K = int(input())

    target = 0
    for i in range(0, 1000000):
        target = target * 10 + 7
        target = target % K

        if target == 0:
            print(i + 1)
            return

    print(-1)


if __name__ == "__main__":
    main()
