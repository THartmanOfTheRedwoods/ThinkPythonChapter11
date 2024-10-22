#!/usr/bin/env python3

if __name__ == '__main__':
    list0 = [1, 2, 3]
    list1 = [4, 5]

    t = (list0, list1)
    t[1].append(6)
    print(t)

    d = {t: "Hello"}  # Causes Type error because immutable tuple contains mutable lists.