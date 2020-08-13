#!/usr/bin/env python3


def main():
    a = int(input())
    bc_ary = input().split()
    b = int(bc_ary[0])
    c = int(bc_ary[1])
    s = input()
    result = str(a + b + c) + " " + s
    print(result)


if __name__ == "__main__":
    main()
