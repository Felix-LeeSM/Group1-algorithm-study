# Leetcode 56. Merge Intervals
#### https://leetcode.com/problems/merge-intervals/

1. Solution
```python
def merge(intervals:List[List[int]]) -> List[List[int]]:
    result = list()
    
    for interval in sorted(intervals):
        # 결과 리스트가 비어있지 않을 때, 구간이 겹칠때 끝 지점 업데이트
        if result and result[-1][1] >= interval[0]:
            result[-1][1] = max(result[-1][1], interval[1])
        # 결과 리스트가 비어있거나, 구간들이 겹치지 않을 때
        else:
            result.append(interval)
            
    return result
```