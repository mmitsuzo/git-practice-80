#!/usr/bin/env python3

# 整数のリストを合計する関数
# function to sum up an int list
def sum_array(array: list) -> int:
    val: int = 0
    for x in array:
        val += x
    return int(val)

x: list[int] = [1, 2, 3, 4]
print(sum_array(x))

