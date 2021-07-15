import sys
T = int(input())
for _ in range(T):                                          # T만큼 반복
    N, M = map(int, input().split())
    a = [int(x) for x in sys.stdin.readline().split()]      # 중요도
    
    copy = list(a)                                          # a리스트 복사
    copy[M] = 'target'                                      # 문서 위치를 target으로 변경
    idx = 0                                                 # target의 위치를 대변할 인덱스

    while 'target' in copy and len(a) > 1:                  # copy안에 target이 있고 a리스트의 길이가 1보다 크다면
        if a[0] >= max(a[1:]):                              # 리스트의 첫번째 중요도가 가장 클때
            a.pop(0)                                        # 위치가 고정되므로 리스트에서 제외
            copy.pop(0)                                     # 복사리스트에서도 삭제
            idx += 1                                        # target위치는 그 이후 일 수 밖에 없으므로 1을 추가

        else:
            a.append(a[0])                                  # 더 큰 값이 뒤에 있다면 가장 뒤로 위치 변경
            a.pop(0)
            copy.append(copy[0])                            # 복사 리스트에서도 위치 변경
            copy.pop(0)

    if 'target' in copy:                                    # copy에 target이 있다는 것은 빠져나가지 못하고 반복문 종료
        idx += 1                                            # 1을 더해줌

    print(idx)