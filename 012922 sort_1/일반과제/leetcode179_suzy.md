# Leetcode 179. Largest Number
#### https://leetcode.com/problems/largest-number/

```python
def to_swap(n1, n2):
    return str(n1) + str(n2) < str(n2) + str(n1)

# i : 정렬해야되는 요소들의 인덱스
# j : 정렬된 요소들의 인덱스
def largestNumber(nums):
    i = 1
    # 1번째 인덱스부터 마지막 인덱스까지 반복
    while i < len(nums):
        # 정렬해야되는 인덱스 바로 앞(=정렬된 마지막 인덱스)부터 비교 & swap
        j = i - 1
        # j = 0이 될때까지 비교 & 조건이 맞으면 swap
        while j >= 0 and to_swap(nums[j], nums[j+1]):
            nums[j], nums[j+1] = nums[j+1], nums[j]
            j -= 1
        i += 1
        
    return str(int(''.join(map(str, nums))))
```