# Chapter17_60. 삽입 정렬 리스트 (500p)
# 난이도 : ★★
# Leet code Num. : 147

# 연결 리스트를 삽입 정렬로 정렬하라

class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution:
    def insertionSortList(self, lst):
        # 두개의 해드를 만든다 한개는 순환할 해드 한개는 고정해드
        # 최적화 공식에서 cur.val 이 None 값이 안나오게 노드에 0을 넣는다.
        cur = par = ListNode(0)
        while lst:
            # 입력받은 리스트의 벨류값을 가지고 정렬된 cur에서 어디에 놓을지 결정한다.
            # cur 의 다음값이 존재하고 그 다음값이 입력값읜 벨류보다 작으면 더 큰값을 찾기위해
            #다음노드로 간다.
            while cur.next and cur.next.val < lst.val:
                cur = cur.next
            #찾은 노드의 다음값에 입력값의 벨류는 넣고 입력값의 다음값에 cur 의 넥스트 노드를 넣어
            #cur 노드와 cur.next 사이에 lst 값을 넣고 lst는 한단계 넘어가준다.
            cur.next, lst.next, lst = lst, cur.next, lst.next
            #최적화를 하기위해서 cur의 벨류가 lst 보다 클때만 해드를 초기값으로 이동해준다.
            #(정렬되있는 cur에서 cur의 벨류가 lst 보다 작으면 현재보다 더 움직여야 알맞은 자리가
            #나옴으로 굳이 초기화를 해줄 필요가 없다.)
            if lst and cur.val > lst.val:
                cur = par
        #처음에 par선언시 0노드부터 시작했기때문에 next 값을 리턴한다.
        return par.next