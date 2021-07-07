import sys

input_list = list(map(int, sys.stdin.readline().split()))   # 구멍의 갯수와 테이프의 길이 리스트
holes = list(map(int, sys.stdin.readline().split()))        # 구멍의 위치 리스트
holes.sort()                                                # 구멍의 위치를 오름차순으로 정렬
tape_cnt = 1                                                # 필요한 테이프 갯수
now_hole = holes[0]                                         # 구멍 위치 계산을 위한 기준

for hole in holes:                                          # 처음 구멍부터 차례대로 반복
    if hole - now_hole >= input_list[1]:                    # 기준과 현재 구멍의 거리가 테이프 길이보다 같거나 크면 == 테이프 하나로 커버 못 함
        tape_cnt += 1                                       # 테이프 갯수를 1개 추가
        now_hole = hole                                     # 현재 구멍이 기준으로 바뀜

print(tape_cnt)                                             # 정답 출력
