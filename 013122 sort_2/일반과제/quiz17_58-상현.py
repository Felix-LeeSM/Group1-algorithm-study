# Chapter17_58. 리스트 정렬 (489p)
# 난이도 : ★★
# Leet code Num. : 148

# 연결리스트를 O(n logn)에 정렬하라
# 예제 1.
# 입력 >> 4 -> 2 -> 1 -> 3
# 출력 >> 1 -> 2 -> 3 -> 4

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def sort(lst):
    # 빈값일때 그냥 반환
    if lst is None:
        return
    # 연결리스트의 값을 받을 리스트 생성
    a = []
    # 리스트의 값을 받아준다.
    while lst:
        a.append(lst.val)
        lst = lst.next
    # 역순서로 정렬한다.
    a.sort(reverse=True)
    # 2개의 동일한 해드를 만든다.
    res = res1 = ListNode()
    # 리스트가 빌때까지 a를 팝하여 res 연결리스트에 삽입한다.
    while a:
        res.next = ListNode(a.pop())
        res = res.next
    # 처음지점 포인트를 고려해 리턴해준다.
    return res1.next
