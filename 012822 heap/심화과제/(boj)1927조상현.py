import sys
# 입력받을 갯수구하기
a = int(input())
b = []
# 입력를 리스트화시키기
for _ in range(a):
    b.append(int(sys.stdin.readline()))
# 인덱스 관리의 편의를 위해 인덱스 0번에 None 값 넣어주기
c = [None]
# 리스트에 넣어진 숫자를 차례로 대입시키기
for i in b:
    # 0이 입력되면 출력
    if i == 0:
        # 리스트 안에 None 만 있으면 0출력후 처음으로 되돌아가기
        if len(c)-1 <1:
            print(0)
            continue
        # 최소힙의 루트와 마지막값을 밖꾸고 팝으로 루트 출력
        c[1], c[-1] = c[-1], c[1]
        print(c.pop())
        # 마지막값이 루트로 갔으니 최소힙을 만들기위해 정렬
        # 인덱스화
        cur = 1
        left = cur * 2
        right = cur * 2 + 1
        par = cur
        # 부모에서 자식으로 내려가는데 자식의 인덱스가 전체 c의 인덱스 이전까지 계산
        while par < len(c) -1:
            #자식이 인덱스 안에 있는지 확인하고 자식이 더 작으면 임시 인덱스에 자식의 인덱스 입력
            if  left <= len(c) -1 and c[par] > c[left]:
                par = left
            if  right <= len(c) -1 and c[par] > c[right]:
                par = right
            # 임시 인덱스와 부모의 인덱스가 다르면 자식이 더 작다는 의미로 서로의 값을 변경
            if par != cur:
                c[par],c[cur] = c[cur],c[par]
                # 변경후 바꾼 자식값에서 다시시작하기 위한 인데싱
                cur = par
                left = cur * 2
                right = cur * 2 + 1
            else:
                #임시 인덱스와 부모 인덱스가 같으면 옳은 위치에 있음으로 정렬화 종료
                break

    else:
        # 입력후 최소힙 정렬
        # 리스트 후미에 입력값 추가
        c.append(i)
        # 후미의 인덱스 번호(자식)와 부모 인덱스 번호 선언
        cur = len(c) -1
        par = cur // 2
        # 부모가 인덱스가 1까지 구하는것을 암시
        while par > 0:
            # 자식이 더 작으면 두 값을 바꿈
            if c[cur] < c[par]:
                c[cur], c[par] = c[par], c[cur]
            # 부모의 값이 자식값이라 지정하고 그 부모의 부모인덱스를 선언
            cur = par
            par = cur // 2
