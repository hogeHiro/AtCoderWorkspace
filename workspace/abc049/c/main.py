#!/usr/bin/env python3
import sys

PARTS = ["eraser", "erase", "dreamer", "dream"]
# PARTS2 = []


def main():
    global PARTS2
    sys.setrecursionlimit(100000)
    S = input()

    # for i in range(0, 4):
    #     for j in range(0, 4):
    #         PARTS2.append(PARTS[i] + PARTS[j])

    # PARTS2 = PARTS2 + PARTS

    if judgeStr2(S):
        print("YES")
    else:
        print("NO")


def judgeStr2(target: str) -> bool:
    currentStr = target
    while currentStr != "":
        isNextOK = False
        for item in PARTS:
            if not currentStr.startswith(item):
                continue

            tempStr = currentStr.replace(item, "", 1)
            if tempStr == "":
                return True

            for item2 in PARTS:
                if tempStr.startswith(item2):
                    isNextOK = True
                    break

            if isNextOK:
                currentStr = tempStr
                break
        if isNextOK:
            continue
        else:
            break
    return currentStr == ""


# 実行時エラーでだめだったやつ（再帰多すぎて遅いらしい）
def judgeStr(target: str) -> bool:
    for item in PARTS:
        if target.startswith(item):
            tempStr = target.replace(item, "", 1)
            if tempStr == "" or judgeStr(tempStr):
                return True

    return False


if __name__ == "__main__":
    main()
