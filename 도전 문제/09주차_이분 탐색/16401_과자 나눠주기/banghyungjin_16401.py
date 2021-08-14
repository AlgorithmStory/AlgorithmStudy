import sys


def is_it_ok(input_snacks, input_length):                       # input_length로 과자를 나누었을 때 나눠지는 과자 개수
    current_snacks = 0                                          # 현재 과자 개수 = 0
    for i in input_snacks:                                      # 과자 리스트 순회
        if current_snacks >= M:                                 # 현재 과자 개수가 필요 개수를 만족하면
            return current_snacks                               # 바로 과자 개수 리턴 후 메소드 종료
        if i >= input_length:                                   # 현재 과자가 input_length 보다 길면
            current_snacks += (i // input_length)               # 나눠 지는 만큼 현재 과자 개수에 더해줌
        else:                                                   # 현재 과자가 input_length 보다 짧으면
            continue                                            # 나눠 지는게 없으므로 다음으로 스킵
    return current_snacks                                       # 전부 순회했으면 과자 개수 리턴


def do_something():                                             # 이분 탐색 메소드
    start = 0                                                   # 최소 길이
    end = snacks[0]                                             # 최대 길이
    answer = 0                                                  # 정답
    while start <= end:                                         # 최소가 최대 보다 클때 = 아직 더 찾을 여지가 있음
        current_snacks = is_it_ok(snacks, (start + end) // 2)   # 최대 최소 길이의 중간 길이로 과자를 나눌 수 있는지 확인
        if current_snacks >= M:                                 # 나눌 수 있으면
            answer = (start + end) // 2                         # 현재 정답 갱신
            start = (start + end) // 2 + 1                      # 다음엔 더 큰 길이로 테스트
        else:                                                   # 나눌 수 없으면
            end = (start + end) // 2 - 1                        # 다음엔 더 작은 길이로 테스트
    return answer                                               # 정답 반환


M, N = map(int, sys.stdin.readline().split())                   # 조카 수, 과자 수 읽어옴
snacks = list(map(int, sys.stdin.readline().split()))           # 과자 길이 리스트 읽어옴
snacks.sort(reverse=True)                                       # 계산 편의를 위해 과자 길이 역순 정렬

if sum(snacks) < M:                                             # 만약 사람이 너무 많아 과자를 못 나누면
    print(0)                                                    # 0 출력
else:                                                           # 아니면
    print(do_something())                                       # 이분 탐색 시작
