def colors(lst):
    # 배운 퀵정렬을 써먹기로 한다.
    def q(lst, start, end):
        # 파티션 선언
        def p(lst, vs, ve):
            # lst[ve]보다 작은 숫자를 움직이는 i 인덱스에 쌓는다.
            i = vs - 1
            for j in range(vs, ve):
                if lst[j] < lst[ve]:
                    i += 1
                    lst[i], lst[j] = lst[j], lst[i]
            # 한바퀴 돌았으니 작은숫자 다음에 lst[ve]를 집어넣는다.
            lst[i + 1], lst[ve] = lst[ve], lst[i + 1]
            # 기준이였던 피봇숫자를 반환한다.
            return i + 1

        if start >= end:
            return None
        pot = p(lst, start, end)
        # 피봇숫자를 이용해 lst 를 2개로 나누어 계산을 이어간다.
        q(lst, start, pot - 1)
        q(lst, pot + 1, end)

    q(lst, 0, len(lst) - 1)
    return lst
