#!/usr/bin/env python3


def main():
    args = input().split()
    N = int(args[0])
    Y = int(args[1])

    for num10000 in range(0, N + 1):
        for num5000 in range(0, N + 1 - num10000):
            num1000 = N - num10000 - num5000
            value = 10000 * num10000 + 5000 * num5000 + 1000 * num1000
            if value == Y:
                print(num10000, num5000, num1000)
                return

    print(-1, -1, -1)


if __name__ == "__main__":
    main()
