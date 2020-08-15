#!/usr/bin/env python3


def main():
    args = input().split()
    a = int(args[0])
    b = int(args[1])
    if (a * b) % 2 == 0:
        print("Even")
    else:
        print("Odd")


if __name__ == "__main__":
    main()
