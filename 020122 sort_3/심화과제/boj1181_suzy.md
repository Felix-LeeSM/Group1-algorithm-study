# BOJ 1181. 단어 정렬
#### https://www.acmicpc.net/problem/1181

1. Solution
```python

import sys

N = int(sys.stdin.readline())
words = [sys.stdin.readline().strip() for _ in range(N)]
words = list(set(words))

words.sort()
words.sort(key=len)

for word in words:
    print(word)

```