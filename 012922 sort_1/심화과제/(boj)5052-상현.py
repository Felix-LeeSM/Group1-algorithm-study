import sys
a = int(input())
for i in range(a):
    b = int(input())
    c = []
    for _ in range(b):
        c.append(sys.stdin.readline().replace(' ','').strip('\n'))
    c.sort()
    d = 0
    for k in range(b-1):
        lan = len(c[k])
        if c[k] == c[k+1][:lan]:
            d = 1
            break
    if d == 0:
        print('YES')
    else:
        print('NO')

