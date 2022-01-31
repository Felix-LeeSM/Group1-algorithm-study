# Leetcode 148. Sort List
#### https://leetcode.com/problems/sort-list/

1. Solution - Quick Sort (memory limit exceeded)

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# linkedList를 list로 만들어서 퀵정렬시키고 다시 linkedList로 연결
def sortList(head): 
    def quicksort(data):
        if len(data) <= 1:
            return data
        
        left, right = list(), list()
        pivot = data[0]
        
        left = [item for item in data[1:] if pivot > item]
        right = [item for item in data[1:] if pivot <= item]
        
        return quicksort(left) + [pivot] + quicksort(right)
    
    # linkedList -> list
    node_list = list()
    node = head
    while node:
        node_list.append(node.val)
        node = node.next
        
    # quick sort
    res = quicksort(node_list)
    
    # list -> linkedList
    node = head
    while node:
        for val in res:
            node.next = ListNode(val)
            node = node.next
    
    return head
```

2. Solution - merge sort
```python
def merge(n0, n1):
    if n0 and n1:
        if n0.val > n1.val:
            n0, n1 = n1, n0
            n0.next = merge(n0.next, n1)

def sortList(head):
    if not (head and head.next):
        return head
    
    half, slow, fast = None, head, head
    while fast and fast.next:
        half, slow, fast = slow, slow.next, fast.next.next
    half.next = None
    
    n0 = sortList(head)
    n1 = sortList(slow)
    
    return merge(n0, n1)
```