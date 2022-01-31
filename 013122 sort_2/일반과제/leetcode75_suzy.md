# Leetcode 75. Sort Colors
#### https://leetcode.com/problems/sort-colors/

1. Quick Sort 3-way Partition (Dijkstra 3-way Quick Sort)
<img src="https://qph.fs.quoracdn.net/main-qimg-94b9dec8f00b69ed6af6ae78accc43c6"/><br>
- v = pivot
- 인자로 들어간 배열을 3등분
  - a[i] < pivot : a[lt] <-> a[i] && lt++ && i++ 
  - a[i] > pivot : a[i] <-> a[gt] && gt--
  - a[i] == pivot : i++


2. Solution
```python
def sortColors(nums):
    # red = lt, white = i, blue = gt
    red, white, blue = 0, 0, len(nums)
    
    # pivot = 1, i <= gt까지 반복하면서 i로 배열 탐색
    while white <= blue:
        # a[i] < pivot
        if nums[white] < 1:
            nums[red], nums[white] = nums[white], nums[red]
            # i++, lt++
            white += 1
            red += 1
        # a[i] > pivot
        elif nums[white] > 1:
            # gt--
            blue -= 1
            nums[white], nums[blue] = nums[blue], nums[white]
        # a[i] == pivot
        else:
            # i++
            white += 1
```