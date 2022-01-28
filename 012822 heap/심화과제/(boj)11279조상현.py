import sys

a = int(input())
b = []
for _ in range(a):
    b.append(int(sys.stdin.readline()))
c = [None]
for i in b:
    if i == 0:
        if len(c)-1 <1:
            print(0)
            continue
        c[1], c[-1] = c[-1], c[1]
        print(c.pop())
        # 송출
        cur = 1
        left = cur * 2
        right = cur * 2 + 1
        par = cur
        while par < len(c) -1:
            if  left <= len(c) -1 and c[par] < c[left]:
                par = left
            if  right <= len(c) -1 and c[par] < c[right]:
                par = right
            if par != cur:
                c[par],c[cur] = c[cur],c[par]
                cur = par
                left = cur * 2
                right = cur * 2 + 1
            else:
                break

    else:
        # 입력후 최소힙 정렬
        c.append(i)
        cur = len(c) -1
        par = cur // 2
        while par > 0:
            if c[cur] > c[par]:
                c[cur], c[par] = c[par], c[cur]
            cur = par
            par = cur // 2
