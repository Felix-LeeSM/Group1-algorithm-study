import heapq

class BinaryMaxHeap:
    def __init__(self):
        # 계산 편의를 위해 0이 아닌 1번째 인덱스부터 사용한다.
        self.items = [None]

    def __len__(self):
        # len() 연산을 가능하게 하는 매직 메서드 덮어쓰기(Override).
        return len(self.items) - 1

    def _percolate_up(self):
        # 인서트한친구는 맨 마지막에 있다.
        cur = len(self)
        # 트리구조에서 자식의 인덱스는 부모의 2배이다.
        par = cur//2
        # 부모가 1보다 작아지면 리스트의 인덱스범위를 벗어난다.
        while par > 0:
            #자식이 더크면 최대힙이므로 부모와 자식을 바꿔준다.
            if self.items[cur] > self.items[par]:
                self.items[cur],self.items[par] = self.items[par],self.items[cur]
            # 한단계 더 높은 인덱스를 설정해준다.
            cur = par
            par = cur//2

    def _percolate_down(self, cur):
        #자식들의 인덱스를 구하고 본인의 인덱스르 복사한다.
        left = cur * 2
        right = cur * 2 +1
        par = cur
        #자식이 부모보다 크다면 복사한 인덱스에 더큰 자식의 인덱스값을 넣어준다.
        if self.items[par] < self.items[left] and left <= len(self):
            par = left
        if self.items[par] > self.items[right] and right <= len(self):
            par = right
        #복사한 인덱스와 입력된 인덱스가 바뀌었으면 부모보다 큰 자식이 있다는것임으로 서로의 값을 바꿔준다.
        #그 다음으로 바꾼 자식노드에서 다시 정렬을 해준다.
        if par != cur:
            self.items[cur],self.items[par] = self.items[par],self.items[cur]
            self._percolate_down(par)



    def insert(self, k):
        #리스트 뒤에 값추가
        self.items.append(k)
        #추가된 리스트 정렬하기
        self._percolate_up()


    def extract(self):
        #1번부터 시작하는 인덱스 반영한다.
        if len(self)<1:
            return None
        #루트와 마지막값을 바꿔준다.
        self.items[1], self.items[-1]= self.items[-1],self.items[1]
        #마지막값장소로 바뀐 루트값을 팝해준다.
        root = self.items.pop()
        #루트값으로 바뀐 마지막값을 정렬해준다.
        self._percolate_down(1)

        return root


def test_maxheap_we_made(lst, k):
    maxheap = BinaryMaxHeap()

    # for 문을 눈여겨봐두세요.
    # 힙정렬 시간복잡도 계산의 토대입니다.
    for elem in lst:
        maxheap.insert(elem)

    return [maxheap.extract() for _ in range(k)][k - 1]

def test_maxheap_heapq(lst, k):
    return heapq.nlargest(k, lst)[-1]

