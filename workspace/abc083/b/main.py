#!/usr/bin/env python3


def main():
    args = input().split()
    N = int(args[0])
    A = int(args[1])
    B = int(args[2])

    counter = 0
    for i in range(1, N + 1):
        sumValue = sum(list(map(lambda x: int(x), list(str(i)))))
        if sumValue >= A and sumValue <= B:
            counter += i

    print(counter)


if __name__ == "__main__":
    main()
