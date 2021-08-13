import sys


def Is_it_ok(input_trees, input_length):                # 해당 높이에서 나무를 잘랐을 때 가져가는 토막의 길이 합을 구하는 메소드
    cut_length = 0                                      # 가져갈 토막의 길이 합
    for i in input_trees:                               # 나무 리스트 순회
        if cut_length >= M:                             # 현재 가져갈 토막의 길이 합이 원하는 것을 만족하면
            return cut_length                           # 리턴
        if i > input_length:                            # 리스트의 나무 높이가 현재 높이보다 크면
            cut_length += (i - input_length)            # 토막 길이에 높이의 차를 더해줌
        else:                                           # 아니면
            return cut_length                           # 더 자를 나무가 없으므로 리턴
    return cut_length                                   # 다 잘랐으면 리턴


def do_something():                                     # 정답을 찾는 메소드
    start = 0                                           # 시작점
    end = trees[0]                                      # 끝점
    answer = (start + end) // 2                         # 정답
    while start <= end:                                 # 시작이 끝 보다 먼저일 때
        now_cut = Is_it_ok(trees, (start + end) // 2)   # 현재 토막의 길이 합 구함
        if now_cut >= M:                                # 길이 합이 원하는 것보다 크거나 같으면
            answer = (start + end) // 2                 # 정답 갱신
            start = (start + end) // 2 + 1              # 더 높은 높이로 갱신
        else:                                           # 길이 합이 원하는 것보다 작으면
            end = (start + end) // 2 - 1                # 더 낮은 높이로 갱신
    return answer                                       # 정답 반환


_, M = map(int, sys.stdin.readline().split())           # 읽어올 거 읽어옴
trees = list(map(int, sys.stdin.readline().split()))    # 나무 리스트 읽어옴
trees.sort(reverse=True)                                # 나무 리스트를 역순 정렬: 토막의 길이 합을 좀더 쉽게 구할 수 있음
print(do_something())                                   # 정답 출력
