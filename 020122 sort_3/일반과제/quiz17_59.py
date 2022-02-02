# Chapter17_59. 구간 병합 (497p)
# 난이도 : ★★
# Leet code Num. : 56

# 겹치는 구간을 병합하라
# 예제 1.
# 입력 >> [[1, 3], [2, 6], [8, 10], [15, 18]]
# 출력 >> [[1, 6], [8, 10], [15, 18]]
import collections


def merge(lst: list[list[int]]):
    lst.sort(key=lambda x: x[0])
    d = collections.deque()
    for a in lst:
        if d:
            e, f = d[-1]
            if e <= a[0] <= f:
                d.pop()
                d.append([min(e, a[0]), max(f, a[1])])
            else:
                d.append(a)
        else:
            d.append(a)

    return list(d)

def merge1( intervals):
    merged = []
    for i in sorted(intervals, key=lambda x: x[0]):
        if merged and i[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], i[1])
        else:
            merged += i,
    return merged

h = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge(h))

