import sys

_ = int(sys.stdin.readline().split()[0])                    # 안쓰는거 읽어옴
input_list = list(map(int, sys.stdin.readline().split()))   # 첫 리스트 읽어옴
input_list.sort()                                           # 첫 리스트 정렬
_ = int(sys.stdin.readline().split()[0])                    # 안쓰는거 읽어옴
find_list = list(map(int, sys.stdin.readline().split()))    # 다음 리스트 읽어옴

for i in find_list:                                         # 다음 리스트 순회
    answer = 0                                              # 정답
    start, end = 0, len(input_list) - 1                     # 시작, 끝점 설정
    while start <= end:                                     # 시작이 끝 보다 앞인 동안
        middle = (start + end) // 2                         # 중간점 계산
        if i == input_list[middle]:                         # 찾고자 하는 값이 중간점이면
            answer = 1                                      # 1 반환
            break                                           # 루프 탈출
        elif i < input_list[middle]:                        # 중간점보다 작으면
            end = middle - 1                                # 끝점을 앞으로 당김
        elif i > input_list[middle]:                        # 중간점보다 크면
            start = middle + 1                              # 시작점을 뒤로 당김
    print(answer)                                           # 정답 출력
