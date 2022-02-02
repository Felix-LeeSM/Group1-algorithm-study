import sys

a = int(input())
b = []
for _ in range(a):
    b.append(sys.stdin.readline().strip('\n'))
c = set(b)
b= list(c)
b.sort(key=lambda x : (len(x),x))

for i in b:
    print(i)