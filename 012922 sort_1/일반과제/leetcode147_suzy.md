# Leetcode 147. Insertion Sort List
#### https://leetcode.com/problems/insertion-sort-list/

- Definition for singly-linked list
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

- Solution
```python
def insertionSortList(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    - cur : 정렬 완료된 노드들의 현재 위치
    - parent
        - 정렬 완료된 노드들의 가장 첫 head
        - 만약 링크드리스트의 head를 parent로 지정할 경우 정렬에 의해 변경될 수 있으니 
        상관없는 더미 노드를 두고, 이 노드.next로 정렬 완료된 노드들을 차례차례 연결한다
    - head : 정렬해야되는 노드의 위치
    """
    
    cur = parent = ListNode(0)
    
    # 정렬해야되는 
    while head:
        # 이미 정렬 완료된 노드의 마지막 값과 정렬해야되는 노드 값을 비교
        # 정렬해야되는 값이 작을 때까지 반복
        while cur.next and cur.next.val < head.val:
            cur = cur.next
        
        # 정렬해야되는 값이 작을 경우 while을 끝내고, cur.next <-> head.next swap
        # 다음 정렬해야하는 값으로 이동해야하므로 head = head.next
        cur.next, head.next, head = head, cur.next, head.next
        
        if head and cur.val > head.val:
            cur = parent
        
    return parent.next
```