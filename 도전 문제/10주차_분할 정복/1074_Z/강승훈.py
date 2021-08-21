# 분할 재귀 함수.
# 입력으로 변의 길이와 그 (변x변)에 해당하는 0,0인덱스를 받음.
def recursion(n_, r_, c_):
    global result_cnt

    # 찾고자 하는 위치에 도달했으면, 출력하고 프로그램 종료.
    if r_ == r and c_ == c:
        print(result_cnt)
        exit(0)

    # 변의 길이가 1이면, 카운트 해줌.
    elif n_ == 1:
        result_cnt += 1
        return

    # 재귀적으로 투입된 파라미터 인덱스가 오리지널 인덱스보다 크면, 분할된 영역에 해당하는 크기 만큼 카운트.
    # 중요한건 최종적으로 찾고자 하는 인덱스가, 분할된 영역에 포함되지 않아야함.
    elif not ((r_ <= r and c_ <= c) and (r < r_+n_ and c < c_+n_)):
        result_cnt += n_*n_
        return
    recursion(n_//2, r_, c_)
    recursion(n_//2, r_, c_+(n_//2))
    recursion(n_//2, r_+(n_//2), c_)
    recursion(n_//2, r_+(n_//2), c_+(n_//2))

# 입력.
n,r,c = map(int, input().split(" "))

# 실행.
result_cnt = 0
recursion(2**n, 0, 0)
